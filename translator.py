from openai import OpenAI

# Connect to LM Studio
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def generate_sql(question):

    prompt = f"""
You are an expert SQL developer.

Database Name: FoodDeliveryDB

Tables:

Customers(
    CustomerID,
    CustomerName,
    Email,
    Phone,
    Address,
    City
)

Restaurants(
    RestaurantID,
    RestaurantName,
    Cuisine,
    Rating,
    Phone,
    Address,
    City
)

MenuItems(
    ItemID,
    RestaurantID,
    ItemName,
    Category,
    Price
)

Orders(
    OrderID,
    CustomerID,
    RestaurantID,
    OrderDate,
    TotalAmount,
    OrderStatus
)

OrderDetails(
    OrderDetailID,
    OrderID,
    ItemID,
    Quantity,
    Price
)

DeliveryPartners(
    PartnerID,
    PartnerName,
    Phone,
    VehicleType,
    Rating
)

Deliveries(
    DeliveryID,
    OrderID,
    PartnerID,
    PickupTime,
    DeliveryTime,
    DeliveryStatus
)

Convert the following English question into a valid Microsoft SQL Server query.

Question:
{question}

Rules:
1. Return ONLY the SQL query.
2. Do NOT use Markdown.
3. Do NOT use ```sql or ``` code fences.
4. Do NOT explain anything.
5. Generate SQL compatible with Microsoft SQL Server.
"""

    response = client.chat.completions.create(
        model="qwen2.5-3b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql = response.choices[0].message.content

    # Remove markdown if the model still returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql