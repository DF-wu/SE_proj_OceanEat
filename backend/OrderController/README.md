# OrderController API Document

## Column Description
+ order_id: TextField, primary key
  + 紀錄訂單的編號
+ customer_id: TextField
  + 紀錄消費者的編號
+ delivery_id: TextField
  + 紀錄外送員的編號
+ order_items: TextField
  + 紀錄訂單的內容
+ destination: TextField
  + 紀錄外送的地址
+ status: BinaryField
  + 紀錄訂單的狀態
+ price: IntegerField
  + 紀錄訂單的總價格