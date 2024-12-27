import streamlit as st
import pandas as pd
import re

#定义面板输入函数
def mb_shuru(shuxing):
    if shuxing == "":
        return 0
    else:
        # 验证输入只包含合法的字符（数字、运算符、小数点、括号等）
        if re.match(r'^[\d\+\-\*/\.\(\)\s]+$', shuxing):
            try:
                # 安全执行输入的数学表达式
                shuxing = eval(shuxing)
            except:
                # 如果输入的表达式有误，返回0
                st.warning("输入的表达式有误，请检查后重新输入。否则此值不生效")
                shuxing = 0
        else:
            # 如果包含非法字符，返回0
            st.warning("输入包含非法字符，请检查是否是英文的括号和乘除法*/，然后重新输入。否则此值不生效")
            shuxing = 0
    return shuxing

#定义百分比输入函数
def bfb_shuru(baifenbi):
    if baifenbi == "":
        return 0
    else:
        # 验证输入只包含合法的字符
        if re.match(r'^[\d\+\-\*/\.\(\)\s]+$', baifenbi):
            try:
                # 计算百分比并返回
                baifenbi = eval(baifenbi) * 0.01
            except:
                baifenbi = 0
                st.warning("输入的表达式有误，请检查后重新输入。否则此值不生效")
        else:
            baifenbi = 0
            st.warning("输入包含非法字符，请检查是否是英文的括号和乘除法*/，然后重新输入。否则此值不生效")
    return baifenbi

# 定义将百分比字符串转化为数值（浮动小数）的函数
def convert_percentage_to_float(percentage_str):
    return float(percentage_str.strip('%')) / 100

#标题
st.title('梦幻模拟战-面板模拟计算器')

# 初始化变量
bz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化白字 字典
lz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化绿字 字典
zw = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化铸纹加成 字典
zyjt = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化职业精通 字典
jjjt = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化竞技精通 字典
wqfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化武器附魔百分比 字典
yffm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化衣服附魔百分比 字典
tsfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化头饰附魔百分比 字典
spfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化饰品附魔百分比 字典
gm_fm_1 = "无"  # 初始化附魔第一套种类
gm_fm_2 = "无"  # 初始化附魔第二套种类
gmfm_bfb = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化共鸣附魔百分比 字典
fm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化附魔总百分比 字典
wqfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化武器附魔固定值 字典
yffm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化衣服附魔固定值 字典
tsfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化头饰附魔固定值 字典
spfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化饰品附魔固定值 字典
fm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化附魔总固定值 字典
wq_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化武器基础值 字典
yf_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化衣服基础值 字典
ts_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化头饰基础值 字典
ts_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化饰品基础值 字典
zb_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化装备基础值总加成 字典

sq_slsb = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契神力石板加成 字典
sq_cxzz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契晨曦之祝加成 字典
sq_cxzz_sbgd = {"士兵生命":"0","士兵攻击":"0","士兵防御":"0","士兵魔防":"0"}  # 过渡 字典 存用户选择的士兵加成百分比
sq_zjc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契总加成 字典

bjl = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化白+绿 字典
zb_tx = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化装备特效加成 字典
zb_tx_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化装备特效 过渡 加成 字典
cjtx = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化超绝特效加成 字典
fm4jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化附魔四件套加成 字典
qtzd_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化其他战斗加成 字典
qtzd_jc_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化其他战斗 过渡 加成 字典
zd_zjc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化战斗总加成 字典
yx_zdmb = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄战斗面板 字典
yx_zdmb_zz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄战斗最终面板（考虑防转攻） 字典
yx_sx_zhl = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄属性转化量 字典
yx_sm_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄生命转化系数 字典
yx_gj_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄攻击转化系数 字典
yx_zl_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄智力转化系数 字典
yx_fy_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄防御转化系数 字典
yx_mf_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄魔防转化系数 字典
yx_jq_zhxs = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄技巧转化系数 字典
yx_sm_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄生命转化系数 过渡 字典
yx_gj_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄攻击转化系数 过渡 字典
yx_zl_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄智力转化系数 过渡 字典
yx_fy_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄防御转化系数 过渡 字典
yx_mf_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄魔防转化系数 过渡 字典
yx_jq_zhxs_gd = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化英雄技巧转化系数 过渡 字典

# 初始化附魔选取的列表
wq_sm_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_gj_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_zl_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_fy_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
wq_mf_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]

yf_sm_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
yf_gj_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
yf_zl_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
yf_fy_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
yf_mf_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

ts_sm_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
ts_gj_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
ts_zl_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
ts_fy_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
ts_mf_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

sp_sm_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_gj_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_zl_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_fy_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_mf_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

wq_sm_gdz_numbers130 = list(range(0, 131))
wq_gj_gdz_numbers30 = list(range(0, 31))
wq_zl_gdz_numbers30 = list(range(0, 31))
wq_fy_gdz_numbers6 = list(range(0, 7))
wq_mf_gdz_numbers6 = list(range(0, 7))

yf_sm_gdz_numbers200 = list(range(0, 201))
yf_gj_gdz_numbers10 = list(range(0, 11))
yf_zl_gdz_numbers10 = list(range(0, 11))
yf_fy_gdz_numbers18 = list(range(0, 19))
yf_mf_gdz_numbers18 = list(range(0, 19))

ts_sm_gdz_numbers200 = list(range(0, 201))
ts_gj_gdz_numbers10 = list(range(0, 11))
ts_zl_gdz_numbers10 = list(range(0, 11))
ts_fy_gdz_numbers18 = list(range(0, 19))
ts_mf_gdz_numbers18 = list(range(0, 19))

sp_sm_gdz_numbers130 = list(range(0, 131))
sp_gj_gdz_numbers20 = list(range(0, 21))
sp_zl_gdz_numbers20 = list(range(0, 21))
sp_fy_gdz_numbers12 = list(range(0, 13))
sp_mf_gdz_numbers12 = list(range(0, 13))

# 分割线
st.divider()

st.write("### 英雄白字区")

@st.cache_data  # 缓存数据，避免重复读取文件
def load_data(file_path):
    df = pd.read_csv(file_path)  # 读取CSV文件
    return df
# 加载数据
csv_file_path = './data/梦战英雄白字.csv'  # 为实际文件路径
df1 = load_data(csv_file_path)

# 英雄选择
hero_names = df1['英雄名'].unique()
selected_hero = st.selectbox("请选择英雄名", hero_names)

# 根据选中英雄，获取职业列表
hero_jobs = df1[df1['英雄名'] == selected_hero]['职业名'].tolist()

# 职业选择框
if hero_jobs:
    selected_job = st.selectbox("请选择职业",hero_jobs)

column01, column02 = st.columns([0.5,1])
with column01:
    # 显示英雄头像
    selected_hero_row = df1[df1['英雄名'] == selected_hero].iloc[0]
    hero_image_url = selected_hero_row['英雄头像']  # 获取头像链接列的值
    # 调整头像大小
    st.image(hero_image_url, caption=selected_hero, width=150)  # 设置宽度为150像素
with column02:
    if selected_hero == "自定义英雄":
        bz["生命"] = st.number_input("生命-白字", value=bz["生命"])  # 生命白字
        bz["攻击"] = st.number_input("攻击-白字", value=bz["攻击"])  # 攻击白字
        bz["智力"] = st.number_input("智力-白字", value=bz["智力"])  # 智力白字
        bz["防御"] = st.number_input("防御-白字", value=bz["防御"])  # 防御白字
        bz["魔防"] = st.number_input("魔防-白字", value=bz["魔防"])  # 魔防白字
        bz["技巧"] = st.number_input("技巧-白字", value=bz["技巧"])  # 技巧白字
    else:
        # 根据选择的英雄和职业，获取属性值
        selected_row = df1[(df1['英雄名'] == selected_hero) & (df1['职业名'] == selected_job)].iloc[0]
        bz = {
            "生命": selected_row["生命"],
            "攻击": selected_row["攻击"],
            "智力": selected_row["智力"],
            "防御": selected_row["防御"],
            "魔防": selected_row["魔防"],
            "技巧": selected_row["技巧"],
        }
        st.markdown(f"#### 生命: {bz["生命"]}")
        st.markdown(f"#### 攻击: {bz["攻击"]}")
        st.markdown(f"#### 智力: {bz["智力"]}")
        st.markdown(f"#### 防御: {bz["防御"]}")
        st.markdown(f"#### 魔防: {bz["魔防"]}")
        st.markdown(f"#### 技巧: {bz["技巧"]}")

# 分割线
st.divider()
st.write("### 神契设置区")

with st.expander("点击打开进行神契设置"):

    # 神契神力石板加成 字典
    sq_slsb_dict = {
        "索尔": {"生命": 360, "攻击": 45, "智力": 45, "防御": 30, "魔防": 30, "技巧": 10, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "菲依雅": {"生命": 180, "攻击": 18, "智力": 75, "防御": 28, "魔防": 50, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "海姆达尔": {"生命": 500, "攻击": 24, "智力": 18, "防御": 82, "魔防": 6, "技巧": 5, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "巴德尔": {"生命": 380, "攻击": 21, "智力": 72, "防御": 46, "魔防": 12, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "奥丁": {"生命": 300, "攻击": 93, "智力": 12, "防御": 36, "魔防": 10, "技巧": 15, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "弗丽嘉": {"生命": 420, "攻击": 18, "智力": 27, "防御": 8, "魔防": 86, "技巧": 5, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "提尔": {"生命": 460, "攻击": 96, "智力": 18, "防御": 28, "魔防": 10, "技巧": 8, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "洛基": {"生命": 400, "攻击": 12, "智力": 120, "防御": 10, "魔防": 18, "技巧": 10, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
        "维达": {"生命": 400, "攻击": 69, "智力": 21, "防御": 14, "魔防": 44, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06}
    }

    # 初始化神契的图片
    sq_tp = {"索尔":"./image/索尔.png","菲依雅":"./image/菲依雅.png","海姆达尔":"./image/海姆达尔.png","巴德尔":"./image/巴德尔.png","奥丁":"./image/奥丁.png","弗丽嘉":"./image/弗丽嘉.png","提尔":"./image/提尔.png","洛基":"./image/洛基.png","维达":"./image/维达.png","未携带":"./image/神契未携带.png"}

    st.write("### 神契神力石板加成")

    # 将神契神力石板加成以表格展示
    df_slsb = pd.DataFrame(sq_slsb_dict).T  # 转置：行是神契，列是属性

    # 将士兵的属性值乘以 100 并添加 '%' 符号
    soldier_columns = ["士兵生命", "士兵攻击", "士兵防御", "士兵魔防"]
    df_slsb[soldier_columns] = df_slsb[soldier_columns].applymap(lambda x: f"{x * 100:.0f}%")

    # 显示表格
    st.dataframe(df_slsb)

    # 初始化结果字典
    result_dict = {}

    st.write("### 神契晨曦之祝加成")
    # 神契晨曦之祝加成
    column1521, column15213, column1522 = st.columns([1,0.2,1])
    with column1521:
        sq_cxzz["生命"] = st.number_input("生命（最大值600）", value=0)  # 生命晨曦绿字
        sq_cxzz["攻击"] = st.number_input("攻击（最大值75）", value=0)  # 攻击晨曦绿字
        sq_cxzz["智力"] = st.number_input("智力（最大值75）", value=0)  # 智力晨曦绿字
    with column1522:
        sq_cxzz["防御"] = st.number_input("防御（最大值60）", value=0)  # 防御晨曦绿字
        sq_cxzz["魔防"] = st.number_input("魔防（最大值60）", value=0)  # 魔防晨曦绿字
        sq_cxzz["技巧"] = st.number_input("技巧（最大值0）", value=0)  # 技巧晨曦绿字
    st.write("")
    column1523, column15223, column1524 = st.columns([1,0.2,1])
    with column1523:
        sq_cxzz["士兵生命"] = bfb_shuru(st.text_input("士兵生命%（最大值18%）", value="0"))  # 士兵生命晨曦加成百分比
        sq_cxzz["士兵攻击"] = bfb_shuru(st.text_input("士兵攻击%（最大值18%）", value="0")) # 士兵攻击晨曦加成百分比
    with column1524:
        sq_cxzz["士兵防御"] = bfb_shuru(st.text_input("士兵防御%（最大值18%）", value="0")) # 士兵防御晨曦加成百分比
        sq_cxzz["士兵魔防"] = bfb_shuru(st.text_input("士兵魔防%（最大值18%）", value="0"))  # 士兵魔防晨曦加成百分比

    # 为每个神契计算总加成
    for sq_name, sq_slsb in sq_slsb_dict.items():
        # 计算每个神契的总加成
        sq_total = {}
        for key in sq_slsb:
            # 进行加成：神力石板加成 + 晨曦之祝加成
            if key in sq_cxzz:
                sq_total[key] = sq_slsb[key] + sq_cxzz[key]  # 加上晨曦之祝的加成
            else:
                sq_total[key] = sq_slsb[key]  # 如果没有晨曦之祝加成，保持原值

        # 将计算结果存入字典
        result_dict[sq_name] = sq_total

    st.write("### 神契总加成")
    tabs = st.tabs(list(sq_slsb_dict.keys()))  # 创建tabs

    # 遍历每个tab，展示神契的总加成
    for tab, sq_name in zip(tabs, sq_slsb_dict.keys()):
        with tab:
            sq_total = result_dict[sq_name]  # 获取该神契的总加成
            sq_image_url = sq_tp[sq_name]  # 获取头像链接列的值
            # 调整头像大小
            st.image(sq_image_url, width=120)  # 设置宽度为120像素

            column153, column154 = st.columns([1, 1])
            with column153:
                st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {sq_total['生命']}</span></strong>", unsafe_allow_html=True)
                st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {sq_total['攻击']}</span></strong>", unsafe_allow_html=True)
                st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {sq_total['智力']}</span></strong>", unsafe_allow_html=True)
            with column154:
                st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {sq_total['防御']}</span></strong>", unsafe_allow_html=True)
                st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {sq_total['魔防']}</span></strong>", unsafe_allow_html=True)
                st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {sq_total['技巧']}</span></strong>", unsafe_allow_html=True)
            column155, column156 = st.columns([1, 1])
            with column155:
                st.markdown(f"#### 士兵生命: <strong><span style='color:green;font-size:25px;'> + {sq_total["士兵生命"]*100}% </span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵攻击: <strong><span style='color:green;font-size:25px;'> + {sq_total["士兵攻击"]*100}% </span></strong>",unsafe_allow_html=True)
            with column156:
                st.markdown(f"#### 士兵防御: <strong><span style='color:green;font-size:25px;'> + {sq_total["士兵防御"]*100}% </span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵魔防: <strong><span style='color:green;font-size:25px;'> + {sq_total["士兵魔防"]*100}% </span></strong>",unsafe_allow_html=True)

# 分割线
st.divider()

st.write("### 英雄绿字区")

tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["装备","附魔","职业精通","铸纹","神契","绿字总加成"])
with tab1:
    column11, column12, column13 = st.columns([1, 0.1, 0.5])
    with column11:
        # 读取 装备基础属性CSV 文件
        file_path = "./data/梦战装备满级基础属性分类.csv"  # 读取CSV文件路径
        df2 = load_data(file_path)

        # 将数据转换为字典，按“名称”索引
        zb_dict = df2.set_index("装备名称").T.to_dict()

        # 筛选数据，根据类型生成选择框
        wq_options = df2[df2["类别"] == "武器"]["装备名称"].tolist()
        yf_options = df2[df2["类别"] == "衣服"]["装备名称"].tolist()
        ts_options = df2[df2["类别"] == "头饰"]["装备名称"].tolist()
        sp_options = df2[df2["类别"] == "饰品"]["装备名称"].tolist()

        # 用户选择框
        yx_wq = st.selectbox("请选择武器", wq_options)
        if yx_wq and yx_wq in zb_dict:
            wq_jc = zb_dict[yx_wq]
            st.markdown(f"武器代表:<span style='color:orange;font-size:16px;'> {zb_dict[yx_wq]['代表']}</span>",unsafe_allow_html=True)  # 显示武器的代表

        yx_yf = st.selectbox("请选择衣服", yf_options)
        if yx_yf and yx_yf in zb_dict:
            yf_jc = zb_dict[yx_yf]
            st.markdown(f"衣服代表:<span style='color:orange;font-size:16px;'>{zb_dict[yx_yf]['代表']}</span>",unsafe_allow_html=True)  # 显示衣服的代表

        yx_ts = st.selectbox("请选择头饰", ts_options)
        if yx_ts and yx_ts in zb_dict:
            ts_jc = zb_dict[yx_ts]
            st.markdown(f"头饰代表:<span style='color:orange;font-size:16px;'> {zb_dict[yx_ts]['代表']}</span>",unsafe_allow_html=True)  # 显示头饰的代表

        yx_sp = st.selectbox("请选择饰品", sp_options)
        if yx_sp and yx_sp in zb_dict:
            sp_jc = zb_dict[yx_sp]
            st.markdown(f"饰品代表:<span style='color:orange;font-size:16px;'> {zb_dict[yx_sp]['代表']}</span>",unsafe_allow_html=True)  # 显示饰品的代表

    with column13:
        # 相加各部分基础值
        zb_jc["生命"] = wq_jc["生命"] + yf_jc["生命"] + ts_jc["生命"] +sp_jc["生命"]
        zb_jc["攻击"] = wq_jc["攻击"] + yf_jc["攻击"] + ts_jc["攻击"] +sp_jc["攻击"]
        zb_jc["智力"] = wq_jc["智力"] + yf_jc["智力"] + ts_jc["智力"] +sp_jc["智力"]
        zb_jc["防御"] = wq_jc["防御"] + yf_jc["防御"] + ts_jc["防御"] +sp_jc["防御"]
        zb_jc["魔防"] = wq_jc["魔防"] + yf_jc["魔防"] + ts_jc["魔防"] +sp_jc["魔防"]
        zb_jc["技巧"] = wq_jc["技巧"] + yf_jc["技巧"] + ts_jc["技巧"] +sp_jc["技巧"]

        # 显示装备基础绿字总加成
        st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {zb_jc["生命"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {zb_jc["攻击"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {zb_jc["智力"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {zb_jc["防御"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {zb_jc["魔防"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {zb_jc["技巧"]}</span></strong>",unsafe_allow_html=True)

with tab2:
    column21,column211,column22,column221,column23 = st.columns([1,0.1,1,0.1,1])
    with column21:
        options_fm = ["无","满月","轻风","时钟","怒涛","魔术","顽石","水晶","寒冰","流星","烈日","大树","荆棘","钢铁"]
        fm_tp = {"满月": "./image/满月.png", "轻风": "./image/轻风.png", "时钟": "./image/时钟.png",
                 "怒涛": "./image/怒涛.png", "魔术": "./image/魔术.png", "顽石": "./image/顽石.png",
                 "水晶": "./image/水晶.png", "寒冰": "./image/寒冰.png", "流星": "./image/流星.png",
                 "烈日": "./image/烈日.png", "大树": "./image/大树.png", "荆棘": "./image/荆棘.png",
                 "钢铁": "./image/钢铁.png"}
        gm_fm_1 = st.selectbox("第一个共鸣2件套",options_fm)

        if gm_fm_1 != "无":
            fm1_image_url1 = fm_tp[gm_fm_1]  # 获取头像链接列的值
            fm1_image_url2 = fm_tp[gm_fm_1]  # 获取头像链接列的值
            # 调整头像大小
            column291,column292 = st.columns([1,1])
            with column291:
                st.image(fm1_image_url1, width=35)  # 设置宽度为35像素
            with column292:
                st.image(fm1_image_url2, width=35)  # 设置宽度为35像素
        gm_fm_2 = st.selectbox("第二个共鸣2件套",options_fm)
        if gm_fm_2 != "无":
            fm2_image_url1 = fm_tp[gm_fm_2]  # 获取头像链接列的值
            fm2_image_url2 = fm_tp[gm_fm_2]  # 获取头像链接列的值
            # 调整头像大小
            column281, column282 = st.columns([1, 1])
            with column281:
                st.image(fm2_image_url1, width=35)  # 设置宽度为35像素
            with column282:
                st.image(fm2_image_url2, width=35)  # 设置宽度为35像素

        gm_fm_jc_1 = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}
        gm_fm_jc_2 = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}

        if gm_fm_1 == "满月" or gm_fm_1 == "轻风" or gm_fm_1 == "时钟" or gm_fm_1 == "怒涛" or gm_fm_1 == "魔术":
            gm_fm_jc_1["攻击"] = 0.05
            gm_fm_jc_1["智力"] = 0.05
        elif gm_fm_1 == "顽石" or gm_fm_1 == "水晶" or gm_fm_1 == "寒冰":
            gm_fm_jc_1["防御"] = 0.05
            gm_fm_jc_1["魔防"] = 0.05
        elif gm_fm_1 == "大树" or gm_fm_1 == "荆棘" or gm_fm_1 == "钢铁":
            gm_fm_jc_1["生命"] = 0.1

        if gm_fm_2 == "满月" or gm_fm_2 == "轻风" or gm_fm_2 == "时钟" or gm_fm_2 == "怒涛" or gm_fm_2 == "魔术":
            gm_fm_jc_2["攻击"] = 0.05
            gm_fm_jc_2["智力"] = 0.05
        elif gm_fm_2 == "顽石" or gm_fm_2 == "水晶" or gm_fm_2 == "寒冰":
            gm_fm_jc_2["防御"] = 0.05
            gm_fm_jc_2["魔防"] = 0.05
        elif gm_fm_2 == "大树" or gm_fm_2 == "荆棘" or gm_fm_2 == "钢铁":
            gm_fm_jc_2["生命"] = 0.1

        gmfm_bfb["生命"] = gm_fm_jc_1["生命"] + gm_fm_jc_2["生命"]
        gmfm_bfb["攻击"] = gm_fm_jc_1["攻击"] + gm_fm_jc_2["攻击"]
        gmfm_bfb["智力"] = gm_fm_jc_1["智力"] + gm_fm_jc_2["智力"]
        gmfm_bfb["防御"] = gm_fm_jc_1["防御"] + gm_fm_jc_2["防御"]
        gmfm_bfb["魔防"] = gm_fm_jc_1["魔防"] + gm_fm_jc_2["魔防"]

        if gm_fm_1 == gm_fm_2:
            gmfm_bfb["生命"] = gmfm_bfb["生命"]/2
            gmfm_bfb["攻击"] = gmfm_bfb["攻击"]/2
            gmfm_bfb["智力"] = gmfm_bfb["智力"]/2
            gmfm_bfb["防御"] = gmfm_bfb["防御"]/2
            gmfm_bfb["魔防"] = gmfm_bfb["魔防"]/2

    with column22:
        with st.expander("武器（百分比）附魔"):
            wqfm_bfb["生命"] = st.selectbox("生命%",wq_sm_bfb_percentages10,index=wq_sm_bfb_percentages10.index("0%"),key="wq_bfb_01") # 武器生命百分比附魔
            wqfm_bfb["攻击"] = st.selectbox("攻击%",wq_gj_bfb_percentages15,index=wq_gj_bfb_percentages15.index("0%"),key="wq_bfb_02") # 武器攻击百分比附魔
            wqfm_bfb["智力"] = st.selectbox("智力%",wq_zl_bfb_percentages15,index=wq_zl_bfb_percentages15.index("0%"),key="wq_bfb_03") # 武器智力百分比附魔
            wqfm_bfb["防御"] = st.selectbox("防御%",wq_fy_bfb_percentages5,index=wq_fy_bfb_percentages5.index("0%"),key="wq_bfb_04") # 武器防御百分比附魔
            wqfm_bfb["魔防"] = st.selectbox("魔防%",wq_mf_bfb_percentages5,index=wq_mf_bfb_percentages5.index("0%"),key="wq_bfb_05") # 武器魔防百分比附魔
        with st.expander("衣服（百分比）附魔"):
            yffm_bfb["生命"] = st.selectbox("生命%",yf_sm_bfb_percentages15,index=yf_sm_bfb_percentages15.index("0%"),key="sf_bfb_01") # 衣服生命百分比附魔
            yffm_bfb["攻击"] = st.selectbox("攻击%",yf_gj_bfb_percentages5,index=yf_gj_bfb_percentages5.index("0%"),key="sf_bfb_02") # 衣服攻击百分比附魔
            yffm_bfb["智力"] = st.selectbox("智力%",yf_zl_bfb_percentages5,index=yf_zl_bfb_percentages5.index("0%"),key="sf_bfb_03") # 衣服智力百分比附魔
            yffm_bfb["防御"] = st.selectbox("防御%",yf_fy_bfb_percentages15,index=yf_fy_bfb_percentages15.index("0%"),key="sf_bfb_04") # 衣服防御百分比附魔
            yffm_bfb["魔防"] = st.selectbox("魔防%",yf_mf_bfb_percentages15,index=yf_mf_bfb_percentages15.index("0%"),key="sf_bfb_05") # 衣服魔防百分比附魔
        with st.expander("头饰（百分比）附魔"):
            tsfm_bfb["生命"] = st.selectbox("生命%",ts_sm_bfb_percentages15,index=ts_sm_bfb_percentages15.index("0%"),key="ts_bfb_01") # 头饰生命百分比附魔
            tsfm_bfb["攻击"] = st.selectbox("攻击%",ts_gj_bfb_percentages5,index=ts_gj_bfb_percentages5.index("0%"),key="ts_bfb_02") # 头饰攻击百分比附魔
            tsfm_bfb["智力"] = st.selectbox("智力%",ts_zl_bfb_percentages5,index=ts_zl_bfb_percentages5.index("0%"),key="ts_bfb_03") # 头饰智力百分比附魔
            tsfm_bfb["防御"] = st.selectbox("防御%",ts_fy_bfb_percentages15,index=ts_fy_bfb_percentages15.index("0%"),key="ts_bfb_04") # 头饰防御百分比附魔
            tsfm_bfb["魔防"] = st.selectbox("魔防%",ts_mf_bfb_percentages15,index=ts_mf_bfb_percentages15.index("0%"),key="ts_bfb_05") # 头饰魔防百分比附魔
        with st.expander("饰品（百分比）附魔"):
            spfm_bfb["生命"] = st.selectbox("生命%",sp_sm_bfb_percentages10,index=sp_sm_bfb_percentages10.index("0%"),key="sp_bfb_01") # 饰品生命百分比附魔
            spfm_bfb["攻击"] = st.selectbox("攻击%",sp_gj_bfb_percentages10,index=sp_gj_bfb_percentages10.index("0%"),key="sp_bfb_02") # 饰品攻击百分比附魔
            spfm_bfb["智力"] = st.selectbox("智力%",sp_zl_bfb_percentages10,index=sp_zl_bfb_percentages10.index("0%"),key="sp_bfb_03") # 饰品智力百分比附魔
            spfm_bfb["防御"] = st.selectbox("防御%",sp_fy_bfb_percentages10,index=sp_fy_bfb_percentages10.index("0%"),key="sp_bfb_04") # 饰品防御百分比附魔
            spfm_bfb["魔防"] = st.selectbox("魔防%",sp_mf_bfb_percentages10,index=sp_mf_bfb_percentages10.index("0%"),key="sp_bfb_05") # 饰品魔防百分比附魔
    with column23:
        with st.expander("武器（固定值）附魔"):
            wqfm_gdz["生命"] = st.selectbox("生命固定值",wq_sm_gdz_numbers130,index=wq_sm_gdz_numbers130.index(0),key="wq_gdz_01") # 武器生命固定值附魔
            wqfm_gdz["攻击"] = st.selectbox("攻击固定值",wq_gj_gdz_numbers30,index=wq_gj_gdz_numbers30.index(0),key="wq_gdz_02") # 武器攻击固定值附魔
            wqfm_gdz["智力"] = st.selectbox("智力固定值",wq_zl_gdz_numbers30,index=wq_zl_gdz_numbers30.index(0),key="wq_gdz_03") # 武器智力固定值附魔
            wqfm_gdz["防御"] = st.selectbox("防御固定值",wq_fy_gdz_numbers6,index=wq_fy_gdz_numbers6.index(0),key="wq_gdz_04") # 武器防御固定值附魔
            wqfm_gdz["魔防"] = st.selectbox("魔防固定值",wq_mf_gdz_numbers6,index=wq_mf_gdz_numbers6.index(0),key="wq_gdz_05") # 武器魔防固定值附魔
        with st.expander("衣服（固定值）附魔"):
            yffm_gdz["生命"] = st.selectbox("生命固定值",yf_sm_gdz_numbers200,index=yf_sm_gdz_numbers200.index(0),key="yf_gdz_01") # 衣服生命固定值附魔
            yffm_gdz["攻击"] = st.selectbox("攻击固定值",yf_gj_gdz_numbers10,index=yf_gj_gdz_numbers10.index(0),key="yf_gdz_02") # 衣服攻击固定值附魔
            yffm_gdz["智力"] = st.selectbox("智力固定值",yf_zl_gdz_numbers10,index=yf_zl_gdz_numbers10.index(0),key="yf_gdz_03") # 衣服智力固定值附魔
            yffm_gdz["防御"] = st.selectbox("防御固定值",yf_fy_gdz_numbers18,index=yf_fy_gdz_numbers18.index(0),key="yf_gdz_04") # 衣服防御固定值附魔
            yffm_gdz["魔防"] = st.selectbox("魔防固定值",yf_mf_gdz_numbers18,index=yf_mf_gdz_numbers18.index(0),key="yf_gdz_05") # 衣服魔防固定值附魔
        with st.expander("头饰（固定值）附魔"):
            tsfm_gdz["生命"] = st.selectbox("生命固定值",ts_sm_gdz_numbers200,index=ts_sm_gdz_numbers200.index(0),key="ts_gdz_01") # 头饰生命固定值附魔
            tsfm_gdz["攻击"] = st.selectbox("攻击固定值",ts_gj_gdz_numbers10,index=ts_gj_gdz_numbers10.index(0),key="ts_gdz_02") # 头饰攻击固定值附魔
            tsfm_gdz["智力"] = st.selectbox("智力固定值",ts_zl_gdz_numbers10,index=ts_zl_gdz_numbers10.index(0),key="ts_gdz_03") # 头饰智力固定值附魔
            tsfm_gdz["防御"] = st.selectbox("防御固定值",ts_fy_gdz_numbers18,index=ts_fy_gdz_numbers18.index(0),key="ts_gdz_04") # 头饰防御固定值附魔
            tsfm_gdz["魔防"] = st.selectbox("魔防固定值",ts_mf_gdz_numbers18,index=ts_mf_gdz_numbers18.index(0),key="ts_gdz_05") # 头饰魔防固定值附魔
        with st.expander("饰品（固定值）附魔"):
            spfm_gdz["生命"] = st.selectbox("生命固定值",sp_sm_gdz_numbers130,index=sp_sm_gdz_numbers130.index(0),key="sp_gdz_01") # 饰品生命固定值附魔
            spfm_gdz["攻击"] = st.selectbox("攻击固定值",sp_gj_gdz_numbers20,index=sp_gj_gdz_numbers20.index(0),key="sp_gdz_02") # 饰品攻击固定值附魔
            spfm_gdz["智力"] = st.selectbox("智力固定值",sp_zl_gdz_numbers20,index=sp_zl_gdz_numbers20.index(0),key="sp_gdz_03") # 饰品智力固定值附魔
            spfm_gdz["防御"] = st.selectbox("防御固定值",sp_fy_gdz_numbers12,index=sp_fy_gdz_numbers12.index(0),key="sp_gdz_04") # 饰品防御固定值附魔
            spfm_gdz["魔防"] = st.selectbox("魔防固定值",sp_mf_gdz_numbers12,index=sp_mf_gdz_numbers12.index(0),key="sp_gdz_05") # 饰品魔防固定值附魔

    #计算总附魔加成
    #百分比总附魔加成
    fm_bfb["生命"] = convert_percentage_to_float(wqfm_bfb["生命"]) + convert_percentage_to_float(yffm_bfb["生命"]) + convert_percentage_to_float(tsfm_bfb["生命"]) + convert_percentage_to_float(spfm_bfb["生命"]) + gmfm_bfb["生命"]
    fm_bfb["攻击"] = convert_percentage_to_float(wqfm_bfb["攻击"]) + convert_percentage_to_float(yffm_bfb["攻击"]) + convert_percentage_to_float(tsfm_bfb["攻击"]) + convert_percentage_to_float(spfm_bfb["攻击"]) + gmfm_bfb["攻击"]
    fm_bfb["智力"] = convert_percentage_to_float(wqfm_bfb["智力"]) + convert_percentage_to_float(yffm_bfb["智力"]) + convert_percentage_to_float(tsfm_bfb["智力"]) + convert_percentage_to_float(spfm_bfb["智力"]) + gmfm_bfb["智力"]
    fm_bfb["防御"] = convert_percentage_to_float(wqfm_bfb["防御"]) + convert_percentage_to_float(yffm_bfb["防御"]) + convert_percentage_to_float(tsfm_bfb["防御"]) + convert_percentage_to_float(spfm_bfb["防御"]) + gmfm_bfb["防御"]
    fm_bfb["魔防"] = convert_percentage_to_float(wqfm_bfb["魔防"]) + convert_percentage_to_float(yffm_bfb["魔防"]) + convert_percentage_to_float(tsfm_bfb["魔防"]) + convert_percentage_to_float(spfm_bfb["魔防"]) + gmfm_bfb["魔防"]
    # 固定值总附魔加成
    fm_gdz["生命"] = wqfm_gdz["生命"] + yffm_gdz["生命"] + tsfm_gdz["生命"] + spfm_gdz["生命"]
    fm_gdz["攻击"] = wqfm_gdz["攻击"] + yffm_gdz["攻击"] + tsfm_gdz["攻击"] + spfm_gdz["攻击"]
    fm_gdz["智力"] = wqfm_gdz["智力"] + yffm_gdz["智力"] + tsfm_gdz["智力"] + spfm_gdz["智力"]
    fm_gdz["防御"] = wqfm_gdz["防御"] + yffm_gdz["防御"] + tsfm_gdz["防御"] + spfm_gdz["防御"]
    fm_gdz["魔防"] = wqfm_gdz["魔防"] + yffm_gdz["魔防"] + tsfm_gdz["魔防"] + spfm_gdz["魔防"]

    #创建附魔加成统计表格 DataFrame
    column24, column25= st.columns([1.2,1])
    with column24:
        st.markdown("""<h5 style='text-align: center;'>附魔百分比加成统计表</h5>""",unsafe_allow_html=True)
        fm_bfb_jc_data = {
            "属性": ["生命", "攻击", "智力", "防御", "魔防"],
            "武器": list(wqfm_bfb.values()),
            "衣服": list(yffm_bfb.values()),
            "头饰": list(tsfm_bfb.values()),
            "饰品": list(spfm_bfb.values()),
            "共鸣": [f"{round(value * 100)}%" for value in gmfm_bfb.values()],
            "合计": [f"{round(value * 100)}%" for value in fm_bfb.values()]
        }
        st.dataframe(fm_bfb_jc_data)
    with column25:
        st.markdown("""<h5 style='text-align: center;'>附魔固定值加成统计表</h5>""",unsafe_allow_html=True)
        fm_gdz_jc_data = {
            "属性": ["生命", "攻击", "智力", "防御", "魔防"],
            "武器": list(wqfm_gdz.values()),
            "衣服": list(yffm_gdz.values()),
            "头饰": list(tsfm_gdz.values()),
            "饰品": list(spfm_gdz.values()),
            "合计": list(fm_gdz.values())
        }
        st.dataframe(fm_gdz_jc_data)

with tab3:
    column31,column32,column33 = st.columns([0.4,1,0.3])
    with column31:
        options_zyjt_sfm = ["默认满", "自定义"]
        zyjt_sfm = st.radio("职业精通是否满值",options_zyjt_sfm)
    with column32:
        if zyjt_sfm == "默认满":
            zyjt["生命"] = 750
            zyjt["攻击"] = 80
            zyjt["智力"] = 80
            zyjt["防御"] = 60
            zyjt["魔防"] = 60
            zyjt["技巧"] = 80
            st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {zyjt["生命"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {zyjt["攻击"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {zyjt["智力"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {zyjt["防御"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {zyjt["魔防"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {zyjt["技巧"]}</span></strong>",unsafe_allow_html=True)
        else:
            zyjt["生命"] = st.number_input("生命-职业精通", value=0)  # 生命职业精通
            zyjt["攻击"] = st.number_input("攻击-职业精通", value=0)  # 攻击职业精通
            zyjt["智力"] = st.number_input("智力-职业精通", value=0)  # 智力职业精通
            zyjt["防御"] = st.number_input("防御-职业精通", value=0)  # 防御职业精通
            zyjt["魔防"] = st.number_input("魔防-职业精通", value=0)  # 魔防职业精通
            zyjt["技巧"] = st.number_input("技巧-职业精通", value=0)  # 技巧职业精通

with tab4:
    column41, column42, column43 = st.columns([0.8, 1, 0.3])
    with column41:
        options_zw_xz = ["无", "攻击英雄", "智力英雄", "双修英雄(火男、黑骑士)", "双修英雄(阿卡娅)","自定义铸纹"]
        zw_xz = st.radio("选择铸纹类型（默认满级）", options_zw_xz)
    with column42:
        if zw_xz == "无":
            zw["生命"] = 0
            zw["攻击"] = 0
            zw["智力"] = 0
            zw["防御"] = 0
            zw["魔防"] = 0
            zw["技巧"] = 0
        elif zw_xz == "攻击英雄":
            zw["生命"] = 1000
            zw["攻击"] = 150
            zw["智力"] = 30
            zw["防御"] = 90
            zw["魔防"] = 90
            zw["技巧"] = 20
        elif zw_xz == "智力英雄":
            zw["生命"] = 1000
            zw["攻击"] = 30
            zw["智力"] = 150
            zw["防御"] = 90
            zw["魔防"] = 90
            zw["技巧"] = 20
        elif zw_xz == "双修英雄(火男、黑骑士)":
            zw["生命"] = 800
            zw["攻击"] = 150
            zw["智力"] = 110
            zw["防御"] = 90
            zw["魔防"] = 90
            zw["技巧"] = 20
        elif zw_xz == "双修英雄(阿卡娅)":
            zw["生命"] = 800
            zw["攻击"] = 110
            zw["智力"] = 150
            zw["防御"] = 90
            zw["魔防"] = 90
            zw["技巧"] = 20
        elif zw_xz == "自定义铸纹":
            zw["生命"] = st.number_input("生命-铸纹加成", value=0)  # 生命铸纹绿字
            zw["攻击"] = st.number_input("攻击-铸纹加成", value=0)  # 攻击铸纹绿字
            zw["智力"] = st.number_input("智力-铸纹加成", value=0)  # 智力铸纹绿字
            zw["防御"] = st.number_input("防御-铸纹加成", value=0)  # 防御铸纹绿字
            zw["魔防"] = st.number_input("魔防-铸纹加成", value=0)  # 魔防铸纹绿字
            zw["技巧"] = st.number_input("技巧-铸纹加成", value=0)  # 技巧铸纹绿字

        if zw_xz != "自定义铸纹":
            st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {zw["生命"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {zw["攻击"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {zw["智力"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {zw["防御"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {zw["魔防"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {zw["技巧"]}</span></strong>",unsafe_allow_html=True)

with tab5:
    st.markdown(f"<span style='color:red;font-size:15px;'>请提前在「神契设置区」设置好神契</span>",unsafe_allow_html=True)

    column569, column568, column567 = st.columns([0.5,1,1])
    with column569:
        # 用户选择框
        list_zdsq = ["未携带","索尔","菲依雅","海姆达尔","巴德尔","奥丁","弗丽嘉","提尔","洛基","维达"]
        selected_sq = st.selectbox("请选择神契",list_zdsq)
    with column568:
        # 显示英雄头像
        sqzd_image_url = sq_tp[selected_sq]  # 获取头像链接列的值
        # 调整头像大小
        st.image(sqzd_image_url,width=120)  # 设置宽度为120像素

    # 获取选中的神契的总加成
    if selected_sq != "未携带":
        sq_zjc = result_dict[selected_sq]
    else:
        sq_zjc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}

    column53, column54 = st.columns([1, 1])
    with column53:
        st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["生命"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["攻击"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["智力"]}</span></strong>",unsafe_allow_html=True)
    with column54:
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["防御"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["魔防"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["技巧"]}</span></strong>",unsafe_allow_html=True)
    column55, column56 = st.columns([1, 1])
    with column55:
        st.markdown(f"#### 士兵生命: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["士兵生命"]*100}% </span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 士兵攻击: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["士兵攻击"]*100}% </span></strong>",unsafe_allow_html=True)
    with column56:
        st.markdown(f"#### 士兵防御: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["士兵防御"]*100}% </span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 士兵魔防: <strong><span style='color:green;font-size:25px;'> + {sq_zjc["士兵魔防"]*100}% </span></strong>",unsafe_allow_html=True)

with tab6:
    lz["生命"] = zb_jc["生命"] + bz["生命"]*fm_bfb["生命"] + fm_gdz["生命"] + zyjt["生命"] + zw["生命"] + sq_zjc["生命"]
    lz["攻击"] = zb_jc["攻击"] + bz["攻击"]*fm_bfb["攻击"] + fm_gdz["攻击"] + zyjt["攻击"] + zw["攻击"] + sq_zjc["攻击"]
    lz["智力"] = zb_jc["智力"] + bz["智力"]*fm_bfb["智力"] + fm_gdz["智力"] + zyjt["智力"] + zw["智力"] + sq_zjc["智力"]
    lz["防御"] = zb_jc["防御"] + bz["防御"]*fm_bfb["防御"] + fm_gdz["防御"] + zyjt["防御"] + zw["防御"] + sq_zjc["防御"]
    lz["魔防"] = zb_jc["魔防"] + bz["魔防"]*fm_bfb["魔防"] + fm_gdz["魔防"] + zyjt["魔防"] + zw["魔防"] + sq_zjc["魔防"]
    lz["技巧"] = zb_jc["技巧"] + zyjt["技巧"] + zw["技巧"] + sq_zjc["技巧"]

    st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {lz["生命"]}</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {lz["攻击"]}</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {lz["智力"]}</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {lz["防御"]}</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {lz["魔防"]}</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {lz["技巧"]}</span></strong>",unsafe_allow_html=True)

# 分割线
st.divider()

st.markdown("""<h5 style='text-align: center;'>英雄绿字加成统计表</h5>""", unsafe_allow_html=True)

# 创建数据表 英雄绿字加成统计表
lz_jc_data = {
    "合计": list(lz.values()),
    "装备基础": list(zb_jc.values()),
    "附魔百分比": [f"{round(value*100)}%" for value in fm_bfb.values()]+["-"] ,
    "附魔百分比*白字": [
        round(bz["生命"]*fm_bfb["生命"],1),
        round(bz["攻击"]*fm_bfb["攻击"],1),
        round(bz["智力"]*fm_bfb["智力"],1),
        round(bz["防御"]*fm_bfb["防御"],1),
        round(bz["魔防"]*fm_bfb["魔防"],1),
        "-",
    ],
    "附魔固定值": list(fm_gdz.values())+["-"],
    "职业精通": list(zyjt.values()),
    "铸纹": list(zw.values()),
    "神契": [
        sq_zjc["生命"],
        sq_zjc["攻击"],
        sq_zjc["智力"],
        sq_zjc["防御"],
        sq_zjc["魔防"],
        sq_zjc["技巧"],
    ],
}

# 将属性作为行索引
df1 = pd.DataFrame(lz_jc_data, index=["生命", "攻击", "智力", "防御", "魔防", "技巧"])

# 显示为DataFrame
st.dataframe(df1,use_container_width=True)

st.image("./image/分割图片.png")  # 设置宽度为150像素

# 分割线
st.divider()

st.write("## 英雄战场面板模拟")

sdsr_pd = st.checkbox("默认关联读取以上英雄模拟结果 (想手动输入 进行下面模拟 就取消勾选)", value=True)

st.divider()

column74, column75 = st.columns([1, 1])

with column74:
    st.write("### 英雄的白+绿面板")
    if sdsr_pd:
        #计算英雄的白+绿
        bjl["生命"] = bz["生命"] + lz["生命"]
        bjl["攻击"] = bz["攻击"] + lz["攻击"]
        bjl["智力"] = bz["智力"] + lz["智力"]
        bjl["防御"] = bz["防御"] + lz["防御"]
        bjl["魔防"] = bz["魔防"] + lz["魔防"]
        bjl["技巧"] = bz["技巧"] + lz["技巧"]

        st.markdown(f"#### 生命: <strong><span style='font-size:25px;'> {bjl["生命"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> {bjl["攻击"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> {bjl["智力"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> {bjl["防御"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> {bjl["魔防"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: <strong><span style='font-size:25px;'> {bjl["技巧"]}</span></strong>",unsafe_allow_html=True)
    else:
        bjl["生命"] = mb_shuru(st.text_input("生命", key="bjl_sm", value="0"))
        bjl["攻击"] = mb_shuru(st.text_input("攻击", key="bjl_gj", value="0"))
        bjl["智力"] = mb_shuru(st.text_input("智力", key="bjl_zl", value="0"))
        bjl["防御"] = mb_shuru(st.text_input("防御", key="bjl_fy", value="0"))
        bjl["魔防"] = mb_shuru(st.text_input("魔防", key="bjl_mf", value="0"))
        bjl["技巧"] = mb_shuru(st.text_input("技巧", key="bjl_jq", value="0"))

with column75:
    st.write("### 英雄竞技精通区")
    column71,column72 = st.columns([0.6, 1])
    with column71:
        st.write("")
        options_jjjt_sfm = ["默认满", "自定义"]
        jjjt_sfm = st.radio("竞技精通是否满值",options_jjjt_sfm)
    with column72:
        if jjjt_sfm == "默认满":
            jjjt["生命"] = 500
            jjjt["攻击"] = 60
            jjjt["智力"] = 60
            jjjt["防御"] = 50
            jjjt["魔防"] = 50
            jjjt["技巧"] = 80
            st.markdown(f"#### 生命: <strong><span style='color:orange;font-size:25px;'> + {jjjt["生命"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 攻击: <strong><span style='color:orange;font-size:25px;'> + {jjjt["攻击"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:orange;font-size:25px;'> + {jjjt["智力"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:orange;font-size:25px;'> + {jjjt["防御"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:orange;font-size:25px;'> + {jjjt["魔防"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 技巧: <strong><span style='color:orange;font-size:25px;'> + {jjjt["技巧"]}</span></strong>",unsafe_allow_html=True)
        else:
            zyjt["生命"] = st.number_input("生命-竞技精通", value=500)  # 生命竞技精通
            zyjt["攻击"] = st.number_input("攻击-竞技精通", value=60)  # 攻击竞技精通
            zyjt["智力"] = st.number_input("智力-竞技精通", value=60)  # 智力竞技精通
            zyjt["防御"] = st.number_input("防御-竞技精通", value=50)  # 防御竞技精通
            zyjt["魔防"] = st.number_input("魔防-竞技精通", value=50)  # 魔防竞技精通
            zyjt["技巧"] = st.number_input("技巧-竞技精通", value=80)  # 技巧竞技精通

# 分割线
st.divider()

options_jjc_pd = ["是", "否"]
jjc_pd = st.radio("是否竞技场", options_jjc_pd)

column81, column82, column83, column84, column85 = st.columns([0.7, 0.9, 0.9, 1, 1])

with column81:
    zb_tx_gd["生命"] = st.text_input("装备特效生命%", value=0)  # 装备特效生命加成百分比
    zb_tx["生命"] = bfb_shuru(zb_tx_gd["生命"])
    zb_tx_gd["攻击"] = st.text_input("装备特效攻击%", value=0)  # 装备特效攻击加成百分比
    zb_tx["攻击"] = bfb_shuru(zb_tx_gd["攻击"])
    zb_tx_gd["智力"] = st.text_input("装备特效智力%", value=0)  # 装备特效智力加成百分比
    zb_tx["智力"] = bfb_shuru(zb_tx_gd["智力"])
    zb_tx_gd["防御"] = st.text_input("装备特效防御%", value=0)  # 装备特效防御加成百分比
    zb_tx["防御"] = bfb_shuru(zb_tx_gd["防御"])
    zb_tx_gd["魔防"] = st.text_input("装备特效魔防%", value=0)  # 装备特效魔防加成百分比
    zb_tx["魔防"] = bfb_shuru(zb_tx_gd["魔防"])
    zb_tx_gd["技巧"] = st.text_input("装备特效技巧%", value=0)  # 装备特效技巧加成百分比
    zb_tx["技巧"] = bfb_shuru(zb_tx_gd["技巧"])

with column82:
    options_cj_pd = ["未开", "开"]
    cj_pd = st.radio("是否开启超绝特效", options_cj_pd)
    if cj_pd == "未开":
        cjtx["攻击"] = 0
        cjtx["智力"] = 0
        cjtx["防御"] = 0
        cjtx["魔防"] = 0
    else:
        cjtx["攻击"] = 0.2
        cjtx["智力"] = 0.2
        cjtx["防御"] = 0.2
        cjtx["魔防"] = 0.3
    st.markdown(f"#### 生命: <strong><span style='font-size:25px;'> +{round(cjtx["生命"]*100)}%</span></strong>",unsafe_allow_html=True)
    if cj_pd == "未开":
        st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> +{round(cjtx["攻击"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> +{round(cjtx["智力"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> +{round(cjtx["防御"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> +{round(cjtx["魔防"]*100)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> +{round(cjtx["攻击"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> +{round(cjtx["智力"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> +{round(cjtx["防御"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> +{round(cjtx["魔防"]*100)}%</span></strong>",unsafe_allow_html=True)
    st.markdown(f"#### 技巧: <strong><span style='font-size:25px;'> +{round(cjtx["技巧"]*100)}%</span></strong>",unsafe_allow_html=True)

with column83:
    if sdsr_pd:
        if gm_fm_1 == "满月" and gm_fm_2 == "满月":
            st.write("#### 附魔：满月")
            fm4jc["攻击"] = 0.1
            fm4jc["智力"] = 0.1
            fm4jc["防御"] = 0.1
            fm4jc["魔防"] = 0.1
        elif gm_fm_1 == "怒涛" and gm_fm_2 == "怒涛":
            st.write("#### 附魔：怒涛")
            fm4jc["攻击"] = 0.1
        elif gm_fm_1 == "大树" and gm_fm_2 == "大树":
            st.write("#### 附魔：大树")
            fm4jc["防御"] = 0.05
            fm4jc["魔防"] = 0.05
        else:
            st.write("#### 附魔无加成")
            fm4jc["生命"] = 0
            fm4jc["攻击"] = 0
            fm4jc["智力"] = 0
            fm4jc["防御"] = 0
            fm4jc["魔防"] = 0
            fm4jc["技巧"] = 0

        st.markdown(f"#### 生命: <strong><span style='font-size:25px;'> +{round(fm4jc["生命"]*100)}%</span></strong>",unsafe_allow_html=True)
        if gm_fm_1 == "满月" and gm_fm_2 == "满月":
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["攻击"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["智力"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["防御"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["魔防"] * 100)}%</span></strong>", unsafe_allow_html=True)
        elif gm_fm_1 == "怒涛" and gm_fm_2 == "怒涛":
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["攻击"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> +{round(fm4jc["智力"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> +{round(fm4jc["防御"] * 100)}%</span></strong>", unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> +{round(fm4jc["魔防"] * 100)}%</span></strong>", unsafe_allow_html=True)
        elif gm_fm_1 == "大树" and gm_fm_2 == "大树":
            st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> +{round(fm4jc["攻击"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> +{round(fm4jc["智力"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["防御"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> +{round(fm4jc["魔防"]*100)}%</span></strong>",unsafe_allow_html=True)
        else:
            st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> +{round(fm4jc["攻击"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> +{round(fm4jc["智力"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> +{round(fm4jc["防御"]*100)}%</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> +{round(fm4jc["魔防"]*100)}%</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: <strong><span style='font-size:25px;'> +{round(fm4jc["技巧"]*100)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.write("#### 附魔加成")
        fm4jc["生命"] = bfb_shuru(st.text_input("生命%", key="fm4jc_sm", value="0"))
        fm4jc["攻击"] = bfb_shuru(st.text_input("攻击%", key="fm4jc_gj", value="0"))
        fm4jc["智力"] = bfb_shuru(st.text_input("智力%", key="fm4jc_zl", value="0"))
        fm4jc["防御"] = bfb_shuru(st.text_input("防御%", key="fm4jc_fy", value="0"))
        fm4jc["魔防"] = bfb_shuru(st.text_input("魔防%", key="fm4jc_mf", value="0"))
        fm4jc["技巧"] = bfb_shuru(st.text_input("技巧%", key="fm4jc_jq", value="0"))


with column84:
    st.write("#### 战场其他加成")
    qtzd_jc_gd["生命"] = st.text_input("战场其他加成生命%", value=0)  # 战斗其他加成生命百分比
    qtzd_jc["生命"] = bfb_shuru(qtzd_jc_gd["生命"])
    qtzd_jc_gd["攻击"] = st.text_input("战场其他加成攻击%", value=0)  # 战斗其他加成攻击百分比
    qtzd_jc["攻击"] = bfb_shuru(qtzd_jc_gd["攻击"])
    qtzd_jc_gd["智力"] = st.text_input("战场其他加成智力%", value=0)  # 战斗其他加成智力百分比
    qtzd_jc["智力"] = bfb_shuru(qtzd_jc_gd["智力"])
    qtzd_jc_gd["防御"] = st.text_input("战场其他加成防御%", value=0)  # 战斗其他加成防御百分比
    qtzd_jc["防御"] = bfb_shuru(qtzd_jc_gd["防御"])
    qtzd_jc_gd["魔防"] = st.text_input("战场其他加成魔防%", value=0)  # 战斗其他加成魔防百分比
    qtzd_jc["魔防"] = bfb_shuru(qtzd_jc_gd["魔防"])
    qtzd_jc_gd["技巧"] = st.text_input("战场其他加成技巧%", value=0)  # 战斗其他加成技巧百分比
    qtzd_jc["技巧"] = bfb_shuru(qtzd_jc_gd["技巧"])

with column85:
    if jjc_pd == "是":
        zd_zjc["生命"] = round(zb_tx["生命"] + cjtx["生命"] + fm4jc["生命"] + qtzd_jc["生命"] + 0.4,1)
    else:
        zd_zjc["生命"] = zb_tx["生命"] + cjtx["生命"] + fm4jc["生命"] + qtzd_jc["生命"]
    zd_zjc["攻击"] = zb_tx["攻击"] + cjtx["攻击"] + fm4jc["攻击"] + qtzd_jc["攻击"]
    zd_zjc["智力"] = zb_tx["智力"] + cjtx["智力"] + fm4jc["智力"] + qtzd_jc["智力"]
    zd_zjc["防御"] = zb_tx["防御"] + cjtx["防御"] + fm4jc["防御"] + qtzd_jc["防御"]
    zd_zjc["魔防"] = zb_tx["魔防"] + cjtx["魔防"] + fm4jc["魔防"] + qtzd_jc["魔防"]
    zd_zjc["技巧"] = zb_tx["技巧"] + cjtx["技巧"] + fm4jc["技巧"] + qtzd_jc["技巧"]

    st.write("### 总加成")
    if zd_zjc["生命"] > 0:
        st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["生命"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["生命"] < 0:
        st.markdown(f"#### 生命: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["生命"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 生命: <strong><span style='font-size:25px;'> +{round(zd_zjc["生命"]*100,1)}%</span></strong>",unsafe_allow_html=True)

    if zd_zjc["攻击"] > 0:
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["攻击"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["攻击"] < 0:
        st.markdown(f"#### 攻击: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["攻击"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> +{round(zd_zjc["攻击"]*100,1)}%</span></strong>",unsafe_allow_html=True)

    if zd_zjc["智力"] > 0:
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["智力"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["智力"] < 0:
        st.markdown(f"#### 智力: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["智力"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> +{round(zd_zjc["智力"]*100,1)}%</span></strong>",unsafe_allow_html=True)

    if zd_zjc["防御"] > 0:
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["防御"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["防御"] < 0:
        st.markdown(f"#### 防御: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["防御"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> +{round(zd_zjc["防御"]*100,1)}%</span></strong>",unsafe_allow_html=True)

    if zd_zjc["魔防"] > 0:
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["魔防"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["魔防"] < 0:
        st.markdown(f"#### 魔防: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["魔防"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> +{round(zd_zjc["魔防"]*100,1)}%</span></strong>",unsafe_allow_html=True)

    if zd_zjc["技巧"] > 0:
        st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> +{round(zd_zjc["技巧"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["技巧"] < 0:
        st.markdown(f"#### 技巧: <strong><span style='color:red;font-size:25px;'> {round(zd_zjc["技巧"]*100,1)}%</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 技巧: <strong><span style='font-size:25px;'> +{round(zd_zjc["技巧"]*100,1)}%</span></strong>",unsafe_allow_html=True)

# 分割线
st.divider()
if jjc_pd == "是":
    yx_zdmb["生命"] = round(bjl["生命"]*(1+zd_zjc["生命"]) + jjjt["生命"],1)
    yx_zdmb["攻击"] = round(bjl["攻击"]*(1+zd_zjc["攻击"]) + jjjt["攻击"],1)
    yx_zdmb["智力"] = round(bjl["智力"]*(1+zd_zjc["智力"]) + jjjt["智力"],1)
    yx_zdmb["防御"] = round(bjl["防御"]*(1+zd_zjc["防御"]) + jjjt["防御"],1)
    yx_zdmb["魔防"] = round(bjl["魔防"]*(1+zd_zjc["魔防"]) + jjjt["魔防"],1)
    yx_zdmb["技巧"] = round(bjl["技巧"]*(1+zd_zjc["技巧"]) + jjjt["技巧"],1)
else:
    yx_zdmb["生命"] = round(bjl["生命"]*(1+zd_zjc["生命"]),1)
    yx_zdmb["攻击"] = round(bjl["攻击"]*(1+zd_zjc["攻击"]),1)
    yx_zdmb["智力"] = round(bjl["智力"]*(1+zd_zjc["智力"]),1)
    yx_zdmb["防御"] = round(bjl["防御"]*(1+zd_zjc["防御"]),1)
    yx_zdmb["魔防"] = round(bjl["魔防"]*(1+zd_zjc["魔防"]),1)
    yx_zdmb["技巧"] = round(bjl["技巧"]*(1+zd_zjc["技巧"]),1)

with st.expander("是否存在 攻转防 防转攻"):
    options_zh_pd = ["增加到某属性", "代替某属性"]
    zh_pd = st.radio("请选择转化方式", options_zh_pd)

    # 分割线
    st.divider()

    yx_sm_fj = st.checkbox("生命进行转化")
    if yx_sm_fj:
        yx_sm_zhxs_gd["攻击"] = st.text_input("生命转化攻击系数%", value=0)
        yx_sm_zhxs["攻击"] = bfb_shuru(yx_sm_zhxs_gd["攻击"])
        yx_sm_zhxs_gd["智力"] = st.text_input("生命转化智力系数%", value=0)
        yx_sm_zhxs["智力"] = bfb_shuru(yx_sm_zhxs_gd["智力"])
        yx_sm_zhxs_gd["防御"] = st.text_input("生命转化防御系数%", value=0)
        yx_sm_zhxs["防御"] = bfb_shuru(yx_sm_zhxs_gd["防御"])
        yx_sm_zhxs_gd["魔防"] = st.text_input("生命转化魔防系数%", value=0)
        yx_sm_zhxs["魔防"] = bfb_shuru(yx_sm_zhxs_gd["魔防"])
        yx_sm_zhxs_gd["技巧"] = st.text_input("生命转化技巧系数%", value=0)
        yx_sm_zhxs["技巧"] = bfb_shuru(yx_sm_zhxs_gd["技巧"])
    yx_gj_fj = st.checkbox("攻击进行转化")
    if yx_gj_fj:
        yx_gj_zhxs_gd["生命"] = st.text_input("攻击转化生命系数%", value=0)
        yx_gj_zhxs["生命"] = bfb_shuru(yx_gj_zhxs_gd["生命"])
        yx_gj_zhxs_gd["智力"] = st.text_input("攻击转化智力系数%", value=0)
        yx_gj_zhxs["智力"] = bfb_shuru(yx_gj_zhxs_gd["智力"])
        yx_gj_zhxs_gd["防御"] = st.text_input("攻击转化防御系数%", value=0)
        yx_gj_zhxs["防御"] = bfb_shuru(yx_gj_zhxs_gd["防御"])
        yx_gj_zhxs_gd["魔防"] = st.text_input("攻击转化魔防系数%", value=0)
        yx_gj_zhxs["魔防"] = bfb_shuru(yx_gj_zhxs_gd["魔防"])
        yx_gj_zhxs_gd["技巧"] = st.text_input("攻击转化技巧系数%", value=0)
        yx_gj_zhxs["技巧"] = bfb_shuru(yx_gj_zhxs_gd["技巧"])
    yx_zl_fj = st.checkbox("智力进行转化")
    if yx_zl_fj:
        yx_zl_zhxs_gd["生命"] = st.text_input("智力转化生命系数%", value=0)
        yx_zl_zhxs["生命"] = bfb_shuru(yx_zl_zhxs_gd["生命"])
        yx_zl_zhxs_gd["攻击"] = st.text_input("智力转化攻击系数%", value=0)
        yx_zl_zhxs["攻击"] = bfb_shuru(yx_zl_zhxs_gd["攻击"])
        yx_zl_zhxs_gd["防御"] = st.text_input("智力转化防御系数%", value=0)
        yx_zl_zhxs["防御"] = bfb_shuru(yx_zl_zhxs_gd["防御"])
        yx_zl_zhxs_gd["魔防"] = st.text_input("智力转化魔防系数%", value=0)
        yx_zl_zhxs["魔防"] = bfb_shuru(yx_zl_zhxs_gd["魔防"])
        yx_zl_zhxs_gd["技巧"] = st.text_input("智力转化技巧系数%", value=0)
        yx_zl_zhxs["技巧"] = bfb_shuru(yx_zl_zhxs_gd["技巧"])
    yx_fy_fj = st.checkbox("防御进行转化")
    if yx_fy_fj:
        yx_fy_zhxs_gd["生命"] = st.text_input("防御转化生命系数%", value=0)
        yx_fy_zhxs["生命"] = bfb_shuru(yx_fy_zhxs_gd["生命"])
        yx_fy_zhxs_gd["攻击"] = st.text_input("防御转化攻击系数%", value=0)
        yx_fy_zhxs["攻击"] = bfb_shuru(yx_fy_zhxs_gd["攻击"])
        yx_fy_zhxs_gd["智力"] = st.text_input("防御转化智力系数%", value=0)
        yx_fy_zhxs["智力"] = bfb_shuru(yx_fy_zhxs_gd["智力"])
        yx_fy_zhxs_gd["魔防"] = st.text_input("防御转化魔防系数%", value=0)
        yx_fy_zhxs["魔防"] = bfb_shuru(yx_fy_zhxs_gd["魔防"])
        yx_fy_zhxs_gd["技巧"] = st.text_input("防御转化技巧系数%", value=0)
        yx_fy_zhxs["技巧"] = bfb_shuru(yx_fy_zhxs_gd["技巧"])
    yx_mf_fj = st.checkbox("魔防进行转化")
    if yx_mf_fj:
        yx_mf_zhxs_gd["生命"] = st.text_input("魔防转化生命系数%", value=0)
        yx_mf_zhxs["生命"] = bfb_shuru(yx_mf_zhxs_gd["生命"])
        yx_mf_zhxs_gd["攻击"] = st.text_input("魔防转化攻击系数%", value=0)
        yx_mf_zhxs["攻击"] = bfb_shuru(yx_mf_zhxs_gd["攻击"])
        yx_mf_zhxs_gd["智力"] = st.text_input("魔防转化智力系数%", value=0)
        yx_mf_zhxs["智力"] = bfb_shuru(yx_mf_zhxs_gd["智力"])
        yx_mf_zhxs_gd["防御"] = st.text_input("魔防转化防御系数%", value=0)
        yx_mf_zhxs["防御"] = bfb_shuru(yx_mf_zhxs_gd["防御"])
        yx_mf_zhxs_gd["技巧"] = st.text_input("魔防转化技巧系数%", value=0)
        yx_mf_zhxs["技巧"] = bfb_shuru(yx_mf_zhxs_gd["技巧"])
    yx_jq_fj = st.checkbox("技巧进行转化")
    if yx_jq_fj:
        yx_jq_zhxs_gd["生命"] = st.text_input("技巧转化生命系数%", value=0)
        yx_jq_zhxs["生命"] = bfb_shuru(yx_jq_zhxs_gd["生命"])
        yx_jq_zhxs_gd["攻击"] = st.text_input("技巧转化攻击系数%", value=0)
        yx_jq_zhxs["攻击"] = bfb_shuru(yx_jq_zhxs_gd["攻击"])
        yx_jq_zhxs_gd["智力"] = st.text_input("技巧转化智力系数%", value=0)
        yx_jq_zhxs["智力"] = bfb_shuru(yx_jq_zhxs_gd["智力"])
        yx_jq_zhxs_gd["防御"] = st.text_input("技巧转化防御系数%", value=0)
        yx_jq_zhxs["防御"] = bfb_shuru(yx_jq_zhxs_gd["防御"])
        yx_jq_zhxs_gd["魔防"] = st.text_input("技巧转化魔防系数%", value=0)
        yx_jq_zhxs["魔防"] = bfb_shuru(yx_jq_zhxs_gd["魔防"])

yx_sx_zhl["生命"] = yx_zdmb["攻击"]*yx_gj_zhxs["生命"] + yx_zdmb["智力"]*yx_zl_zhxs["生命"] + yx_zdmb["防御"]*yx_fy_zhxs["生命"] + yx_zdmb["魔防"]*yx_mf_zhxs["生命"]+ yx_zdmb["技巧"]*yx_jq_zhxs["生命"]
yx_sx_zhl["攻击"] = yx_zdmb["生命"]*yx_sm_zhxs["攻击"] + yx_zdmb["智力"]*yx_zl_zhxs["攻击"] + yx_zdmb["防御"]*yx_fy_zhxs["攻击"] + yx_zdmb["魔防"]*yx_mf_zhxs["攻击"]+ yx_zdmb["技巧"]*yx_jq_zhxs["攻击"]
yx_sx_zhl["智力"] = yx_zdmb["生命"]*yx_sm_zhxs["智力"] + yx_zdmb["攻击"]*yx_gj_zhxs["智力"] + yx_zdmb["防御"]*yx_fy_zhxs["智力"] + yx_zdmb["魔防"]*yx_mf_zhxs["智力"]+ yx_zdmb["技巧"]*yx_jq_zhxs["智力"]
yx_sx_zhl["防御"] = yx_zdmb["生命"]*yx_sm_zhxs["防御"] + yx_zdmb["攻击"]*yx_gj_zhxs["防御"] + yx_zdmb["智力"]*yx_zl_zhxs["防御"] + yx_zdmb["魔防"]*yx_mf_zhxs["防御"]+ yx_zdmb["技巧"]*yx_jq_zhxs["防御"]
yx_sx_zhl["魔防"] = yx_zdmb["生命"]*yx_sm_zhxs["魔防"] + yx_zdmb["攻击"]*yx_gj_zhxs["魔防"] + yx_zdmb["智力"]*yx_zl_zhxs["魔防"] + yx_zdmb["防御"]*yx_fy_zhxs["魔防"]+ yx_zdmb["技巧"]*yx_jq_zhxs["魔防"]
yx_sx_zhl["技巧"] = yx_zdmb["生命"]*yx_sm_zhxs["技巧"] + yx_zdmb["攻击"]*yx_gj_zhxs["技巧"] + yx_zdmb["智力"]*yx_zl_zhxs["技巧"] + yx_zdmb["防御"]*yx_fy_zhxs["技巧"]+ yx_zdmb["魔防"]*yx_mf_zhxs["技巧"]

if zh_pd == "增加到某属性":
    yx_zdmb_zz["生命"] = yx_zdmb["生命"] + yx_sx_zhl["生命"]
    yx_zdmb_zz["攻击"] = yx_zdmb["攻击"] + yx_sx_zhl["攻击"]
    yx_zdmb_zz["智力"] = yx_zdmb["智力"] + yx_sx_zhl["智力"]
    yx_zdmb_zz["防御"] = yx_zdmb["防御"] + yx_sx_zhl["防御"]
    yx_zdmb_zz["魔防"] = yx_zdmb["魔防"] + yx_sx_zhl["魔防"]
    yx_zdmb_zz["技巧"] = yx_zdmb["技巧"] + yx_sx_zhl["技巧"]
else:
    if yx_sx_zhl["生命"] != 0:
        yx_zdmb_zz["生命"] = yx_sx_zhl["生命"]
    if yx_sx_zhl["攻击"] != 0:
        yx_zdmb_zz["攻击"] = yx_sx_zhl["攻击"]
    if yx_sx_zhl["智力"] != 0:
        yx_zdmb_zz["智力"] = yx_sx_zhl["智力"]
    if yx_sx_zhl["防御"] != 0:
        yx_zdmb_zz["防御"] = yx_sx_zhl["防御"]
    if yx_sx_zhl["魔防"] != 0:
        yx_zdmb_zz["魔防"] = yx_sx_zhl["魔防"]
    if yx_sx_zhl["技巧"] != 0:
        yx_zdmb_zz["技巧"] = yx_sx_zhl["技巧"]

st.write("### 英雄的战场面板")

column91, column92, column93= st.columns([1, 1, 1])
with column91:
    if zd_zjc["生命"] > 0 or yx_sx_zhl["生命"]!= 0:
        st.markdown(f"### 生命: <strong><span style='color:green;font-size:35px;'> {yx_zdmb_zz["生命"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["生命"] < 0:
        st.markdown(f"### 生命: <strong><span style='color:red;font-size:35px;'> {yx_zdmb_zz["生命"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"### 生命: <strong><span style='font-size:35px;'> {yx_zdmb_zz["生命"]}</span></strong>",unsafe_allow_html=True)
with column92:
    if zd_zjc["攻击"] > 0 or yx_sx_zhl["攻击"]!= 0:
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> {yx_zdmb_zz["攻击"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["攻击"] < 0:
        st.markdown(f"#### 攻击: <strong><span style='color:red;font-size:25px;'> {yx_zdmb_zz["攻击"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 攻击: <strong><span style='font-size:25px;'> {yx_zdmb_zz["攻击"]}</span></strong>",unsafe_allow_html=True)
    if zd_zjc["防御"] > 0 or yx_sx_zhl["防御"]!= 0:
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> {yx_zdmb_zz["防御"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["防御"] < 0:
        st.markdown(f"#### 防御: <strong><span style='color:red;font-size:25px;'> {yx_zdmb_zz["防御"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 防御: <strong><span style='font-size:25px;'> {yx_zdmb_zz["防御"]}</span></strong>",unsafe_allow_html=True)
    if zd_zjc["技巧"] > 0 or yx_sx_zhl["技巧"]!= 0:
        st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> {yx_zdmb_zz["技巧"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["技巧"] < 0:
        st.markdown(f"#### 技巧: <strong><span style='color:red;font-size:25px;'> {yx_zdmb_zz["技巧"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 技巧: <strong><span style='font-size:25px;'> {yx_zdmb_zz["技巧"]}</span></strong>",unsafe_allow_html=True)
with column93:
    if zd_zjc["智力"] > 0 or yx_sx_zhl["智力"]!= 0:
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> {yx_zdmb_zz["智力"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["智力"] < 0:
        st.markdown(f"#### 智力: <strong><span style='color:red;font-size:25px;'> {yx_zdmb_zz["智力"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 智力: <strong><span style='font-size:25px;'> {yx_zdmb_zz["智力"]}</span></strong>",unsafe_allow_html=True)
    if zd_zjc["魔防"] > 0 or yx_sx_zhl["魔防"]!= 0:
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> {yx_zdmb_zz["魔防"]}</span></strong>",unsafe_allow_html=True)
    elif zd_zjc["魔防"] < 0:
        st.markdown(f"#### 魔防: <strong><span style='color:red;font-size:25px;'> {yx_zdmb_zz["魔防"]}</span></strong>",unsafe_allow_html=True)
    else:
        st.markdown(f"#### 魔防: <strong><span style='font-size:25px;'> {yx_zdmb_zz["魔防"]}</span></strong>",unsafe_allow_html=True)

# 分割线
#st.divider()

#st.write("### 英雄兵修区（未开发）")
#sm_bx = st.number_input("生命-兵修", 0)  # 生命兵修
#gj_bx = st.number_input("攻击-兵修", 0)  # 攻击兵修
#fy_bx = st.number_input("防御-兵修", 0)  # 防御兵修
#mf_bx = st.number_input("魔防-兵修", 0)  # 魔防兵修




