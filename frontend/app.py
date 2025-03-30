import streamlit as st
import requests
import pandas as pd

# 🎨 Apply Custom CSS for Styling
st.markdown("""
    <style>
        html {
            background-color: #71797E;
        }
        div.stButton > button {
            background-color: steelblue;
            color: white;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
        }
        div.stAlert {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

BASE_URL = "http://127.0.0.1:8000/api"

st.markdown("<h3>📦 Inventory Management - Products</h3>", unsafe_allow_html=True)

# Function to fetch all products
def get_products():
    try:
        response = requests.get(f"{BASE_URL}/products/")  # ✅ Ensure trailing slash
        #st.write("🔍 API Response Status:", response.status_code)  # ✅ Debug
        #st.write("🔍 API Response JSON:", response.json())  # ✅ Debug

        return response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Error fetching products: {e}")
        return []


# Function to add a product
def add_product(name, category, price, stock):
    data = {"name": name, "category": category, "price": price, "stock": stock}
    response = requests.post(f"{BASE_URL}/products/", json=data)
    return response.json()


# Function to update product
def update_product(product_id, price, stock):
    data = {}
    if price is not None and price > 0.01:  # Ensure price is valid
        data["price"] = price
    if stock is not None:  # Always allow stock updates
        data["stock"] = stock

    if not data:
        return {"message": "⚠️ No valid fields to update!"}

    response = requests.put(f"{BASE_URL}/products/{product_id}", json=data)
    return response.json()


# Function to delete a product
def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    return response.json()


# 📌 Tabs for different operations
tab1, tab2, tab3, tab4 = st.tabs(["📋 View Products", "➕ Add Product", "✏️ Update Product", "🗑️ Delete Product"])

# 🟢 Tab 1: View Products
with tab1:
    st.subheader("📋 Products List")

    if st.button("🔄 Refresh", key="refresh_button"):
        st.rerun()

    products = get_products()  # Fetch products from API

    if products:
        df = pd.DataFrame(products)
        #st.write("📊 Dataframe Preview:", df)  # Debugging: Print DataFrame
        st.dataframe(df, hide_index=True)  # Display table
    else:
        st.warning("⚠️ No products found or API response is empty.")

# 🔵 Tab 2: Add Product
with tab2:
    st.subheader("➕ Add New Product")
    name = st.text_input("Product Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.01, format="%.2f")
    stock = st.number_input("Stock", min_value=0, step=1)

    if st.button("Add Product", key="add_product_button"):
        result = add_product(name, category, price, stock)
        st.success(result.get("message", "✅ Product added successfully!"))
        st.rerun()

# 🟡 Tab 3: Update Product
with tab3:
    st.subheader("✏️ Update Product Details")
    product_id = st.number_input("Product ID", min_value=1, step=1)
    new_price = st.number_input("New Price", min_value=0.01, format="%.2f")
    new_stock = st.number_input("New Stock", min_value=0, step=1)

    if st.button("Update Product", key="update_product_button"):
        result = update_product(product_id, new_price, new_stock)
        st.success(result.get("message", "✅ Product updated successfully!"))
        st.rerun()


# 🔴 Tab 4: Delete Product (Confirmation)
with tab4:  # ✅ Correct tab reference
    st.subheader("🗑️ Delete Product")

    delete_id = st.number_input("🔢 Enter Product ID to Delete", min_value=1, step=1)

    if "confirm_delete" not in st.session_state:
        st.session_state.confirm_delete = False  # Initialize session state

    # Click "Delete Product" -> Shows confirmation buttons
    if st.button("🗑️ Delete Product", key="delete_product_button"):
        if delete_id:
            st.session_state.confirm_delete = True
        else:
            st.warning("⚠️ Please enter a valid Product ID.")

    # If user confirms delete
    if st.session_state.confirm_delete:
        st.warning(f"⚠️ Are you sure you want to delete Product ID {delete_id}?")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("✅ Yes, Delete", key="confirm_delete_button"):
                if delete_id:
                    result = delete_product(delete_id)
                    st.success(result.get("message", "✅ Product deleted successfully!"))
                else:
                    st.error("❌ Invalid Product ID")

                st.session_state.confirm_delete = False  # Reset confirmation
                st.rerun()

        with col2:
            if st.button("❌ Cancel", key="cancel_delete_button"):
                st.session_state.confirm_delete = False  # Reset confirmation
                st.rerun()
