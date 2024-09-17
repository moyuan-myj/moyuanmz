import math
import streamlit as st
import re

#标题
st.title('梦幻模拟战简易计算器')

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


#定义攻方攻击
gf_gj = st.text_input("攻方攻击","0")
gf_gj = mb_shuru(gf_gj)

#定义攻方智力
gf_zl = st.text_input("攻方智力","0")
gf_zl = mb_shuru(gf_zl)

#定义守方防御
sf_fy = st.text_input("守方防御","0")
sf_fy = mb_shuru(sf_fy)

#定义守方魔防
sf_mf = st.text_input("守方魔防","0")
sf_mf = mb_shuru(sf_mf)

#定义攻方技能倍率
gf_jnbl = st.text_input("攻方技能倍率","0")
gf_jnbl = mb_shuru(gf_jnbl)

#定义通用增减伤
ty_zjs = st.text_input("通用增减伤%","0")
ty_zjs = bfb_shuru(ty_zjs)

#定义技能增减伤
jn_zjs = st.text_input("技能增减伤%","0")
jn_zjs = bfb_shuru(jn_zjs)

#定义远程增减伤
yc_zjs = st.text_input("远程增减伤%","0")
yc_zjs = bfb_shuru(yc_zjs)

#定义其他增减伤
qt_zjs = st.text_input("其他增减伤%","0")
qt_zjs = bfb_shuru(qt_zjs)

#定义攻方攻智克制系数
gf_gzkzxs = st.text_input("攻方攻智克制系数%","0")
gf_gzkzxs = bfb_shuru(gf_gzkzxs)

#定义攻方无视防御系数
gf_wsfyxs = st.text_input("攻方无视防御系数%","0")
gf_wsfyxs = bfb_shuru(gf_wsfyxs)

#定义守方双防克制系数
sf_sfkzxs = st.text_input("守方双防克制系数%","0")
sf_sfkzxs = bfb_shuru(sf_sfkzxs)

#定义守方地形
sf_dx = st.selectbox("守方地形",("无地形","树林","城墙","山地","基岩","货物","沙丘","礁石","石柱"))

#定义守方地形修正 sf_dxxz
#根据地形判断地形修正
if sf_dx == "无地形":
    sf_dxxz = 0
elif sf_dx == "树林":
    sf_dxxz = 0.2
elif sf_dx == "城墙":
    sf_dxxz = 0.3
elif sf_dx == "山地":
    sf_dxxz = 0.1
elif sf_dx == "基岩":
    sf_dxxz = 0.2
elif sf_dx == "货物":
    sf_dxxz = 0.15
elif sf_dx == "沙丘":
    sf_dxxz = 0.1
elif sf_dx == "礁石":
    sf_dxxz = 0.05
else:
    sf_dxxz = 0.05
#输出地形修正
st.write(f"守方地形修正为: <font color=red>{sf_dxxz*100}%</font>",unsafe_allow_html=True)

#攻击系数
gf_gjxs = st.radio("攻击系数（单点为0.5，AOE为10，水狗1.5）",(0.5,10,1.5))

#攻击段数
gf_gjds = st.radio("攻击段数（正常单点20，AOE为1，水狗6）",(20,1,6))

#选择物理还是魔法伤害
sh_lx = st.radio("选择伤害类型",("物理伤害","魔法伤害"))

#定义攻方暴伤加成
gf_bs = st.text_input("攻方暴伤加成%","0")
gf_bs = bfb_shuru(gf_bs)

#定义守方减暴伤
sf_jbs = st.text_input("守方减暴伤%","0")
sf_jbs = bfb_shuru(sf_jbs)

#定义单段伤害 sh_dd
#定义总伤害 sh_zs
#定义单段暴击伤害 bjsh_dd
#定义暴击总伤害 bjsh_zs

if sh_lx == "物理伤害":
#计算物理伤害
    sh_dd = (gf_gj*(1+gf_gzkzxs) - sf_fy*(1+sf_sfkzxs+sf_dxxz)*(1-gf_wsfyxs)) * gf_jnbl * (1+ty_zjs) * (1+jn_zjs) * (1+yc_zjs) * (1+qt_zjs) * gf_gjxs
    sh_zs = sh_dd * gf_gjds
    bjsh_dd = sh_dd * (1.3+gf_bs-sf_jbs)
    bjsh_zs = bjsh_dd * gf_gjds
else:
#计算魔法伤害
    sh_dd = (gf_zl*(1+gf_gzkzxs) - sf_mf*(1+sf_sfkzxs+sf_dxxz)*(1-gf_wsfyxs)) * gf_jnbl * (1+ty_zjs) * (1+jn_zjs) * (1+yc_zjs) * (1+qt_zjs) * gf_gjxs
    sh_zs = sh_dd * gf_gjds
    bjsh_dd = sh_dd * (1.3 + gf_bs - sf_jbs)
    bjsh_zs = bjsh_dd * gf_gjds

st.write("### 单段伤害为",f"<h2><font color=red>{sh_dd}</font></h2>",unsafe_allow_html=True)
st.write("### 总伤害为",f"<h2><font color=green>{sh_zs}</font></h2>",unsafe_allow_html=True)
st.write("### 暴击单段伤害为",f"<h2><font color=orange>{bjsh_dd}</font></h2>",unsafe_allow_html=True)
st.write("### 暴击总伤害为",f"<h2><font color=brown>{bjsh_zs}</font></h2>",unsafe_allow_html=True)

#分割线
st.divider()

st.write("使用说明：")
st.write("1.面板和增伤都是可以代入公式计算的，如要算一个士兵的攻击面板，可以直接输入233*(1+0.2+0.3)*1.4。但注意一定要使用英文的括号和英文的* /乘除法。")
st.write("2.增减伤、克制系数、无视克制都是默认百分比形式，如增伤应输入“20+5+8”，如克制系数如果是魔力震荡打圣职应输入“50”。")
st.write("3.增减伤需要判断正负号，如兰迪远程减伤光环，应在远程增减伤乘区输入“-15”。")
st.write("4.物理和魔法伤害需要手动选择，物理伤害默认用攻击-防御，魔法伤害默认用智力-魔防，如像尤弥尔这类物理转魔法，应将尤弥尔的攻击填到智力处，不然不能正常生效。")
st.write("5.如果没有出数据，检查是不是技能倍率没填，普攻要填1。")
st.write("6.如有站地形需要手动选择地形，或自己手动在“守方双防克制系数”填入地形加成系数。")
st.write("7.无视防御系数默认为无视双防，物理和魔法伤害计算均生效，仍为填入百分比，如水晶锋刺，应填入20。")
st.write("8.使用期间可能用诸多问题，建议作为测试机制，模拟经验使用。战场千遍万化靠的是经验，如实战使用翻车，不承担任何责任。")
st.write("单点版将网址中的 jsq 替换为 ddjsq ，梦战计算器使用交流群 928411216")