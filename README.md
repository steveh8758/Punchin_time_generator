# Punchin_time_generator

## Usage
> 自動建立打卡時間。

1. 自動避開打卡時間個位數不為 0, 5 的時間。
2. DATE 可以以 [10, 15] 匹配 10, 11, 12, 13, 14, 15。
3. DATE_TEMPLATE 輸入，已修改時間串。
4. TOTAL_HOUR 可更改需要打多長時間。
5. NEED_SPLIT 設置後會以 15 行為分割。

## DEMO
```python
NEED_SPLIT = True
TOTAL_HOUR = 20
DATE_TEMPLATE = r"2025/4/"
DATE = [[1,31]]
```

```
2025/4/1	08:18	10:59	
2025/4/1	14:14	18:47	
2025/4/2	08:14	12:17	
2025/4/2	15:52	19:31	
2025/4/3	08:38	11:24	
2025/4/3	14:54	18:08	

Total time: 20 hr 56 min
```