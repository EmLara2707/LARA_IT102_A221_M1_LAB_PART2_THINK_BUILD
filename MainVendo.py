import streamlit as st
from Items import Items
from Transactions import Transactions
from Vendo import Vendo

st.set_page_config(page_title = "Water Refilling Vendo", layout = "centered")

if "vendo" not in st.session_state:
    st.session_state.vendo = Vendo()

vendo = st.session_state.vendo

st.title(f"{vendo.name}")
st.write("Select a container, enter your payment, and get your change.")

st.divider()

st.subheader("Available Container")
cols = st.columns(len(vendo.getContainerNames()))
for col, name in zip(cols, vendo.getContainerNames()):
    item = vendo.getContainer(name)
    with col:
        st.metric(label=item.container, value=f"₱{item.price:.2f}")

st.divider()

st.subheader("Make a Purchase")
selected_name = st.selectbox("Select an item:", vendo.getContainerNames())
selected_item = vendo.getContainer(selected_name)
 
st.write(f"Price: **₱{selected_item.price:.2f}**")
 
payment = st.number_input(
    "Enter payment amount (₱):",
    min_value=0.0,
    step=1.0,
    format="%.2f",
)
 
if st.button("Buy", type="primary"):
    transaction = vendo.processTransactions(selected_name, payment)
 
    st.write("---")
    st.write(f"**Selected Container:** {selected_item.container}")
    st.write(f"**Price:** ₱{selected_item.price:.2f}")
    st.write(f"**Payment:** ₱{payment:.2f}")
 
    if transaction.noChange():
        change = transaction.change()
        st.success(f"✅ Dispensing {selected_item.container}. Your change is ₱{change:.2f}")
        transaction.change_breakdown()
    else:
        st.error("❌ Insufficient payment.")