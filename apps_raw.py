apps = [
    {
        "app_name": "Weather",
        "app_function": [
            "View current weather forecasts for the current city and surrounding areas",
            "Provide weather forecasts for the next few hours and days",
            "Display weather indicators such as temperature, humidity, wind speed, and direction",
            "Provide life indices such as air quality, clothing suggestions, etc.",
            "Support weather inquiries for multiple cities",
            "Can set cities of interest for easy viewing of weather conditions in different areas",
        ],
        "launch_command": "com.huawei.android.totemweather/.WeatherMainActivity",
    },
    {
        "app_name": "baidu map",
        "app_function": [
            "Find places and routes: Search for specific places, view maps, and get route guidance.",
            "Real-time navigation: Provide real-time navigation guidance to help users reach their destination.",
            "Surrounding service information: Display information about nearby shops, restaurants, hospitals, etc.",
            "Public transportation information: Provide information on public transportation routes, schedules, and fares.",
            "Bookmark and mark locations: Users can bookmark frequently visited places and mark important locations on the map.",
            "Real-time traffic conditions: Display real-time traffic conditions to help users choose the best route.",
            "Voice navigation: Support voice navigation to facilitate user operation during driving.",
        ],
        "launch_command": "com.baidu.maps.caring/com.baidu.baidumaps.MapsActivity",
    },
    {
        "app_name": "calculator",
        "app_function": [
            "Basic arithmetic operations: Addition, subtraction, multiplication, and division.",
            "Scientific functions: Trigonometric functions, logarithms, square roots, etc.",
            "Memory functions: Store and recall numbers for calculations.",
            "Percentage calculations: Calculate percentages of numbers.",
            "History tracking: View and recall previous calculations.",
            "Customization options: Adjust settings for precision, display format, etc.",
            "Unit conversions: Convert between different units of measurement.",
        ],
        "launch_command": "com.huawei.calculator/.Calculator",
    },
    {
        "app_name": "Didi",
        "app_function": [
            "Scheduled rides: Can schedule travel time and location in advance, convenient for the elderly to arrange trips.",
            "Instant rides: Support calling nearby available vehicles anytime, anywhere, to meet immediate travel needs.",
            "View vehicle location: View the real-time location and distance of nearby vehicles on the map.",
            "Choose vehicle type: Can choose different types of vehicles according to needs, such as Comfort, Luxury, etc.",
            "Payment methods: Support multiple payment methods, including online payment and cash payment.",
            "Driver rating: After the ride, passengers can rate the driver to help improve service quality.",
            "Safety features: Provide emergency contact and trip sharing features to increase travel safety.",
        ],
        "launch_command": "com.sdu.didi.psnger/com.didi.sdk.app.launch.splash.SplashActivity",
    },
    {
        "app_name": "Feizhu",
        "app_function": [
            "Search, compare, and book transportation such as flights, train tickets, bus tickets, etc.",
            "Browse and book accommodation services such as hotels, homestays, etc.",
            "View tourist attractions information and book tickets",
            "Plan and manage travel plans, including itinerary arrangements and budget management",
            "Get real-time travel reminders and itinerary change notifications",
            "Pay reservation fees online",
        ],
        "launch_command": "com.taobao.trip/.home.HomeActivity",
        # 由于权限问题无法启动
    },
    {
        "app_name": "Alipay",
        "app_function": [
            "Mobile payment: Support online payment, transfer, and payment of utilities, credit card bills, etc.",
            "Financial management: Provide wealth management, insurance, and other financial services.",
            "Life services: Can pay for water and electricity bills, phone bills, and other daily expenses.",
            "Discounts and coupons: Provide various discounts and coupons for shopping and dining.",
            "Scan code payment: Support scanning code payment in physical stores and online shopping.",
            "Fund transfer: Can transfer money to friends and family through the app.",
            "Investment services: Provide investment and financial planning services.",
        ],
        "launch_command": "com.eg.android.AlipayGphone/.AlipayLogin",
    },
    {
        "app_name": "camera",
        "app_function": [
            "Take photos: Capture photos by clicking the capture button",
            "Record videos: Record video clips, long-press the capture button to start recording",
            "View photos and videos: View captured photos and videos in the gallery",
            "Edit photos: Provide basic photo editing functions such as cropping, rotating, applying filters, etc.",
            "Share photos and videos: Share captured content via social media, messaging apps, etc.",
            "Settings: Adjust camera parameters such as flash, gridlines, etc.",
        ],
        "launch_command": "com.huawei.camera/com.huawei.camera",
    },
    {
        "app_name": "calendar",
        "app_function": [
            "Schedule management: Create, edit, and delete events, appointments, and reminders.",
            "Event notifications: Receive reminders and notifications for upcoming events and tasks.",
            "Multiple calendar views: Switch between daily, weekly, monthly, and yearly views for better planning.",
            "Sync with other devices: Synchronize calendar data with other devices for easy access and backup.",
            "Customizable settings: Adjust settings for event colors, notifications, time zones, etc.",
            "Holiday calendars: Display national holidays and festivals for reference.",
            "Task lists: Create to-do lists and manage tasks within the calendar app.",
        ],
        "launch_command": "com.android.calendar/.AllInOneActivity",
    },
    {
        "app_name": "duolingo",
        "app_function": [
            "Language learning: Provide courses in various languages to help users learn new languages.",
            "Listening exercises: Practice listening skills by listening to spoken sentences and selecting the correct translation.",
            "Speaking exercises: Practice speaking skills by repeating sentences and comparing pronunciation.",
            "Writing exercises: Practice writing skills by typing translations of sentences.",
            "Vocabulary exercises: Learn new words and phrases through vocabulary exercises.",
            "Progress tracking: Track learning progress and receive feedback on performance.",
            "Daily goals: Set daily learning goals to stay motivated and consistent.",
        ],
        "launch_command": "com.duolingo/.app.LoginActivity",
    },
    {
        "app_name": "cainiao",
        "app_function": [
            "Parcel tracking: Track the status and location of parcels in real-time.",
            "Delivery services: Schedule package pickup and delivery services.",
            "Address book: Manage sender and recipient addresses for easy order placement.",
            "Payment options: Support various payment methods for shipping fees and services.",
            "Customer service: Access customer support for inquiries, complaints, and feedback.",
            "Notifications: Receive notifications on package status updates and delivery schedules.",
            "User account: Create and manage user accounts for personalized services.",
        ],
        "launch_command": "com.cainiao.wireless/.homepage.view.activity.HomePageActivity",
    },
    {
        "app_name": "taobao",
        "app_function": [
            "Online shopping: Browse, search, and purchase products from various categories.",
            "Discounts and promotions: Receive discounts, coupons, and promotions for shopping.",
            "Order tracking: Track the status of orders, view order history, and manage returns.",
            "Store browsing: Explore different online stores, view product details, and read reviews.",
            "Payment options: Support various payment methods, including Alipay, credit cards, etc.",
            "Customer service: Contact customer service for inquiries, complaints, and feedback.",
            "Product recommendations: Receive personalized product recommendations based on browsing history.",
        ],
        "launch_command": "com.taobao.taobao/com.taobao.tao.welcome.Welcome",
    },
    {
        "app_name": "美团",
        "app_description": "本地生活，可以点外卖、订酒店、打车等等",
        "launch_command": "com.sankuai.meituan/com.meituan.android.pt.homepage.activity.MainActivity",
    },
    {
        "app_name": "时钟",
        "app_description": "查看时间、定闹钟、计时、查看世界时钟",
        "launch_command": "com.android.deskclock/.AlarmsMainActivity",
    },
    {
        "app_name": "相册",
        "app_description": "浏览和整理照片或视频、分享照片或视频给其他人、编辑照片或视频",
        "launch_command": "com.android.gallery3d/com.huawei.gallery.app.GalleryMain",
    },
    {
        "app_name": "计算器",
        "app_description": "科学计算数字",
        "launch_command": "com.huawei.calculator/com.huawei.calculator.Calculator",
    },
    {
        "app_name": "微信",
        "app_description": "聊天、朋友圈、小程序",
        "launch_command": "com.tencent.mm/com.tencent.mm.ui.LauncherUI",
    },
    {
        "app_name": "通讯录",
        "app_description": "保存联系人、寻找联系人、删去联系人、更新联系人页面信息",
        "launch_command": "com.android.contacts/com.android.contacts.activities.PeopleActivity",
    },
    {
        "app_name": "电话",
        "app_description": "拨打电话",
        "launch_command": "com.android.contacts/.activities.DialtactsActivity",
    },
    {
        "app_name": "信息",
        "app_description": "发送短信",
        "launch_command": "com.android.mms/.ui.ConversationList",
    },
    {
        "app_name": "抖音",
        "app_description": "浏览短视频、制作分享短视频给好友、搜索查看短视频",
        "launch_command": "com.ss.android.ugc.aweme/.splash.SplashActivity",
    },
    {
        "app_name": "淘宝",
        "app_description": "浏览商品、购买商品和分享商品",
        "launch_command": "com.taobao.taobao/com.taobao.tao.TBMainActivity",
    },
    {
        "app_name": "京东",
        "app_description": "浏览商品、购买商品和分享商品",
        "launch_command": "com.jingdong.app.mall/.main.MainActivity",
    },
    {
        "app_name": "腾讯视频",
        "app_description": "观看电影电视剧",
        "launch_command": "com.tencent.qqlive/.ona.activity.SplashHomeActivity",
    },
    {
        "app_name": "12306",
        "app_function": [
            "Train ticket booking: Search, book, and purchase train tickets for domestic travel.",
            "Ticket inquiry: Check train schedules, ticket availability, and prices.",
            "Order management: Manage booked tickets, view order details, and make changes or cancellations.",
            "Seat selection: Choose preferred seat types and locations when booking tickets.",
            "Payment methods: Support online payment and ticket collection methods.",
            "Ticket verification: Provide ticket verification codes for boarding.",
            "Service hotline: Access customer service for inquiries and assistance.",
        ],
        "launch_command": "com.MobileTicket/.ui.activity.MainActivity",
        # 由于权限问题无法启动
    },
    # {
    #     "app_name": "手电筒",
    #     "app_description": "打开手电筒",
    #     "launch_command": "com.android.systemui/com.android.systemui.flashlight.FlashlightActivity",
    # },打开错误，Permission Denial
    # {
    #     "app_name": "应用商店",
    #     "app_description": "下载和更新手机应用",
    #     "launch_command": "com.huawei.appmarket/.MarketActivity",
    # },adb打开失败：Permission Denial
    # {
    #             "app_name": "拼多多",
    #             "app_description": "浏览商品、购买商品和分享商品",
    #             "launch_command": "com.xunmeng.pinduoduo/.ui.activity.HomeActivity",
    #         },adb打开失败：Permission Denial
    # {
    #     "app_name": "支付宝",
    #     "app_description": "支付、转账、理财、生活服务",
    #     "launch_command": "com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin"
    # },
    # {
    #     "app_name": "快手",
    #     "app_description": "浏览短视频、制作分享短视频给好友、搜索查看短视频",
    # },{
    #     "app_name": "爱奇艺",
    #     "app_description": "观看电影电视剧",
    # },{
    #     "app_name": "优酷视频",
    #     "app_description": "观看电影电视剧",
    # },{
    #     "app_name": "酷狗音乐",
    #     "app_description": "搜索收听歌曲、听歌识曲",
    # },{
    #     "app_name": "今日头条",
    #     "app_description": "获取新闻资讯、浏览新闻资讯",
    # }
]
