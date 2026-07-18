DATABASE_SCHEMA = """
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
    City,
    IsActive,
    CreatedAt
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
"""