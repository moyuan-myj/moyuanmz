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

# 在代码开头初始化三个空列表用于存储伤害值
if 'saved_damage_yxdyx' not in st.session_state:
    st.session_state.saved_damage_yxdyx = [] #英雄打英雄伤害存储列表
if 'saved_damage_yxdb' not in st.session_state:
    st.session_state.saved_damage_yxdb = [] #英雄打士兵伤害存储列表
if 'saved_damage_zsh' not in st.session_state:
    st.session_state.saved_damage_zsh = [] #总伤害存储列表

# 初始化存储护盾值的列表
if 'saved_hudun_cs_value' not in st.session_state:
    st.session_state.saved_hudun_cs_value = [] #护盾承伤值的存储列表(总承伤)
if 'saved_hudun_yxdyx_cs_value' not in st.session_state:
    st.session_state.saved_hudun_yxdyx_cs_value = [] #护盾承伤值的存储列表(英雄打英雄)
if 'saved_hudun_yxdb_cs_value' not in st.session_state:
    st.session_state.saved_hudun_yxdb_cs_value = [] #护盾承伤值的存储列表(英雄打兵)

#标题
st.title('梦幻模拟战-AOE模拟计算器')

column1, column2, column3 = st.columns([1,0.3,1])

with column1:
    st.write("### 攻方")
    # 定义攻方英雄攻击
    gf_yxgj = st.text_input("攻方英雄攻击", "0")
    gf_yxgj = mb_shuru(gf_yxgj)
    # 定义攻方英雄智力
    gf_yxzl = st.text_input("攻方英雄智力", "0")
    gf_yxzl = mb_shuru(gf_yxzl)

    yx_yxdyx_kzpd = st.checkbox("英雄与英雄 有克制关系")
    if yx_yxdyx_kzpd:
        # 定义攻方英雄对英雄攻智克制系数
        gf_yxdyx_gzkzxs = st.text_input("英雄对英雄攻智克制系数加成%", "0")
        gf_yxdyx_gzkzxs = bfb_shuru(gf_yxdyx_gzkzxs)
    else:
        gf_yxdyx_gzkzxs = 0
    yx_yxdb_kzpd = st.checkbox("英雄与兵 有克制关系")
    if yx_yxdb_kzpd:
        # 定义攻方英雄对士兵攻智克制系数
        gf_yxdsb_gzkzxs = st.text_input("英雄对士兵攻智克制系数加成%", "0")
        gf_yxdsb_gzkzxs = bfb_shuru(gf_yxdsb_gzkzxs)
    else:
        gf_yxdsb_gzkzxs = 0

    column21, column22 = st.columns([1, 1])
    with column21:
        # 选择物理还是魔法伤害
        yxsh_lx = st.radio("英雄伤害类型", ("物理", "魔法"))
    with column22:
        # 定义攻方英雄无视双防系数
        gf_yx_wsfy = st.text_input("无视双防系数%", "0")
        gf_yx_wsfy = bfb_shuru(gf_yx_wsfy)
    # 定义攻方英雄技能倍率
    gf_yxjnbl = st.text_input("攻方英雄技能倍率（别忘记填，不填没伤害）", "0")
    gf_yxjnbl = mb_shuru(gf_yxjnbl)
    # 定义攻方英雄物理通用增伤
    gf_yx_tyzs = st.text_input("攻方英雄通用增伤%", "0")
    gf_yx_tyzs = bfb_shuru(gf_yx_tyzs)
    column23, column24 = st.columns([1, 1])
    with column23:
        # 定义攻方英雄技能增伤
        gf_yx_jnzs = st.text_input("攻方英雄技能增伤%", "0")
        gf_yx_jnzs = bfb_shuru(gf_yx_jnzs)
        # 定义攻方英雄远程增伤
        gf_yx_yczs = st.text_input("攻方英雄远程增伤%", "0")
        gf_yx_yczs = bfb_shuru(gf_yx_yczs)
    with column24:
        # 定义攻方英雄其他增伤
        gf_yx_qtzs = st.text_input("攻方英雄其他增伤%", "0")
        gf_yx_qtzs = bfb_shuru(gf_yx_qtzs)
        # 定义攻方英雄暴伤加成
        gf_yx_bs = st.text_input("攻方英雄暴伤加成%", "0")
        gf_yx_bs = bfb_shuru(gf_yx_bs)

with column3:
    st.write("### 守方")
    tab3, tab4 = st.tabs(["英雄", "士兵"])
    with tab3:
        # 定义守方英雄防御
        sf_yxfy = st.text_input("守方英雄防御", "0")
        sf_yxfy = mb_shuru(sf_yxfy)
        # 定义守方英雄魔防
        sf_yxmf = st.text_input("守方英雄魔防", "0")
        sf_yxmf = mb_shuru(sf_yxmf)

        if yx_yxdyx_kzpd:
            # 定义守方英雄与攻方英雄交战时双防克制系数加成
            sf_yxdyx_sfkzxs = st.text_input("英雄与 攻方英雄 交战时双防克制系数加成%", "0")
            sf_yxdyx_sfkzxs = bfb_shuru(sf_yxdyx_sfkzxs)
        else:
            sf_yxdyx_sfkzxs = 0

        # 定义守方英雄通用减伤
        sf_yx_tyjs = st.text_input("守方英雄通用减伤%", "0")
        sf_yx_tyjs = bfb_shuru(sf_yx_tyjs)

        column41, column42 = st.columns([1, 1])
        with column41:
            # 定义守方英雄技能减伤
            sf_yx_jnjs = st.text_input("守方英雄技能减伤%", "0")
            sf_yx_jnjs = bfb_shuru(sf_yx_jnjs)
            # 定义守方英雄远程减伤
            sf_yx_ycjs = st.text_input("守方英雄远程减伤%", "0")
            sf_yx_ycjs = bfb_shuru(sf_yx_ycjs)
        with column42:
            # 定义守方英雄其他减伤
            sf_yx_qtjs = st.text_input("守方英雄其他减伤%", "0")
            sf_yx_qtjs = bfb_shuru(sf_yx_qtjs)
            # 定义守方英雄减暴伤
            sf_yx_jbs = st.text_input("守方英雄减暴伤%", "0")
            sf_yx_jbs = bfb_shuru(sf_yx_jbs)

    with tab4:
        # 定义守方士兵防御
        sf_sbfy = st.text_input("守方士兵防御", "0")
        sf_sbfy = mb_shuru(sf_sbfy)
        # 定义守方士兵魔防
        sf_sbmf = st.text_input("守方士兵魔防", "0")
        sf_sbmf = mb_shuru(sf_sbmf)

        if yx_yxdb_kzpd:
            # 定义守方士兵与攻方英雄交战时双防克制系数加成
            sf_sbdyx_sfkzxs = st.text_input("士兵与 攻方英雄 交战时双防克制系数加成%", "0")
            sf_sbdyx_sfkzxs = bfb_shuru(sf_sbdyx_sfkzxs)
        else:
            sf_sbdyx_sfkzxs = 0

        # 定义守方士兵通用减伤
        sf_sb_tyjs = st.text_input("守方士兵通用减伤%", "0")
        sf_sb_tyjs = bfb_shuru(sf_sb_tyjs)

        column33, column34 = st.columns([1, 1])
        with column33:
            # 定义守方士兵技能减伤
            sf_sb_jnjs = st.text_input("守方士兵技能减伤%", "0")
            sf_sb_jnjs = bfb_shuru(sf_sb_jnjs)
            # 定义守方士兵远程减伤
            sf_sb_ycjs = st.text_input("守方士兵远程减伤%", "0")
            sf_sb_ycjs = bfb_shuru(sf_sb_ycjs)
        with column34:
            # 定义守方士兵其他减伤
            sf_sb_qtjs = st.text_input("守方士兵其他减伤%", "0")
            sf_sb_qtjs = bfb_shuru(sf_sb_qtjs)
            # 定义守方士兵减暴伤
            sf_sb_jbs = st.text_input("守方士兵减暴伤%", "0")
            sf_sb_jbs = bfb_shuru(sf_sb_jbs)

    # 分割线
    st.divider()

    # 定义守方地形
    sf_dx = st.selectbox("守方地形", ("无地形", "树林", "城墙", "山地", "基岩", "货物", "沙丘", "礁石", "石柱"))
    # 定义守方地形修正 sf_dxxz
    # 根据地形判断地形修正
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
    # 输出地形修正
    st.write(f"守方地形修正为: <font color=red>{sf_dxxz*100}%</font>",unsafe_allow_html=True)

# 分割线
st.divider()

with st.expander("（点击打开查看）神契晨曦之祝特效参考"):
    chakan_sq = pd.DataFrame(
        {"神契": ["菲依雅", "", "", "索尔", "", "", "海姆达尔", "", "", "巴德尔", "", "", "奥丁", "", "", "弗丽嘉",
                  "",
                  "", "提尔", "", "", "洛基", "", "", "维达", "", ""],
         "神祈特效": ["主动进入战斗造成魔法伤害提升2%~8%", "主动进入战斗时，目标越远伤害越高，最高提升2%~8%",
                      "主动进入战斗前未进行过移动，伤害提升2%~8%",
                      "范围伤害提升2%~8%", "进入战斗暴击率提升2%~10%", "固定伤害提升2%~10%",
                      "进入战斗遭受物理伤害降低2%~8%", "自身相邻有友军时，进入战斗遭受伤害降低1%~6%",
                      "反击伤害提升2%~10%", "遭受范围伤害降低2%~8%", "受到固定伤害降低2%~10%",
                      "主动进入战斗防御，魔防提升2%~8%", "主动进入战斗造成物理伤害提升2%~8%",
                      "范围技能命中3名及以上敌军时造成伤害提升1%~6%", "进入战斗前移动越远伤害越高，最高提升2%~8%",
                      "进入战斗时，目标越远遭受伤害越低，最多降低2%~8%", "进入战斗遭受魔法伤害降低2%~8%",
                      "部队生命低于100%时，遭受范围伤害降低2%~8%",
                      "与有弱化效果的敌军进入战斗时，造成物理伤害提升2%~8%",
                      "与克制的敌军进入战斗时，造成物理伤害提升2%~8%", "进入战斗暴击伤害提升2%~10%",
                      "与有弱化效果的敌军进入战斗时，造成魔法伤害提升2%~8%",
                      "与克制的敌军进入战斗时，造成魔法伤害提升2%~8%", "进入战斗遭受暴击率降低2%~10%",
                      "被近战攻击进入战斗时，遭受伤害降低2%~8%", "被远程攻击进入战斗时，遭受伤害降低1%~6%",
                      "进入战斗遭受暴击伤害降低2%~10%"]})
    st.dataframe(chakan_sq)

with st.expander("（点击打开查看）职业克制系数参考"):
    chakan_kzxs = pd.DataFrame(
        {"进攻\防守": ["枪兵", "步兵", "骑兵", "飞兵", "水兵", "弓兵", "法师", "僧侣", "魔物"],
         "枪兵": ["", "+40%", "-30%", "", "", "", "","", ""],
         "步兵": ["-20%", "", "+20%", "", "", "", "", "", ""],
         "骑兵": ["+30%", "-30%", "", "", "", "", "", "", ""],
         "飞兵": ["", "", "", "", "", "+30%", "", "", ""],
         "水兵": ["", "", "", "", "", "", "", "", ""],
         "弓兵": ["", "", "", "", "", "", "", "", ""],
         "法师": ["", "", "", "", "", "", "", "", ""],
         "僧侣": ["", "", "", "", "", "", "", "", "-40%"],
         "魔物": ["", "", "", "", "", "", "","+80%", ""]})
    st.dataframe(chakan_kzxs)

with st.expander("（点击打开查看）与AOE有关的士兵科技参考"):
    chakan_sbkj = pd.DataFrame( {"士兵种类": ["步兵",  "步兵",  "枪兵", "枪兵", "骑兵","飞兵","弓兵","法师", "僧兵", "僧兵", "魔物"],
             "科技名称": ["对枪特训", "应急处理", "对骑特训", "作战续行","对步特训","特技飞行","密林游侠", "圣光护佑","对魔特训", "圣光护佑", "污秽铠甲"],
             "科技效果": ["对枪兵士兵攻防克制修正+30%", "士兵大于80%血，减伤20%","对骑兵士兵攻防克制修正+30%","士兵低于70%血时,减伤20%","对步兵士兵攻智防克制修正+30%","站地形时,减伤+20%","对飞兵士兵攻防克制修正+30%","部队满血时，减伤30%","对魔物士兵攻防克制修正+30%", "部队满血时，减伤30%","常驻双防+20%，但与魔物或僧侣交战时，双防克制修正-16%"]})
    st.dataframe(chakan_sbkj)

# 分割线
st.divider()

#定义英雄打兵AOE伤害 yxdb_aoe_sh
#定义英雄打兵AOE暴击伤害 yxdb_aoebj_sh
#定义英雄打英雄AOE伤害 yxdyx_aoe_sh
#定义英雄打英雄AOE暴击伤害 yxdyx_aoebj_sh

if yxsh_lx == "物理":
#计算英雄打兵物理伤害
    yxdb_aoe_sh = (gf_yxgj*(1+gf_yxdsb_gzkzxs) - sf_sbfy*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 10
    yxdb_aoebj_sh = yxdb_aoe_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄物理伤害
    yxdyx_aoe_sh = (gf_yxgj*(1+gf_yxdyx_gzkzxs) - sf_yxfy*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 10
    yxdyx_aoebj_sh = yxdyx_aoe_sh * (1.3+gf_yx_bs-sf_yx_jbs)
else:
#计算英雄打兵魔法伤害
    yxdb_aoe_sh = (gf_yxzl*(1+gf_yxdsb_gzkzxs) - sf_sbmf*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 10
    yxdb_aoebj_sh = yxdb_aoe_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄魔法伤害
    yxdyx_aoe_sh = (gf_yxzl*(1+gf_yxdyx_gzkzxs) - sf_yxmf*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 10
    yxdyx_aoebj_sh = yxdyx_aoe_sh * (1.3+gf_yx_bs-sf_yx_jbs)

column4, column5, column6 = st.columns([1,0.1,1])

with column4:
    st.markdown(f"##### 英雄打英雄伤害为 <strong><span style='color:green;font-size:25px;'>{round(yxdyx_aoe_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打英雄暴击伤害为 <strong><span style='color:orange;font-size:25px;'>{round(yxdyx_aoebj_sh, 2)}</span></strong>", unsafe_allow_html=True)

with column6:
    st.markdown(f"##### 英雄打兵伤害为 <strong><span style='color:blue;font-size:25px;'>{round(yxdb_aoe_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打兵暴击伤害为 <strong><span style='color:orange;font-size:25px;'>{round(yxdb_aoebj_sh, 2)}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

st.markdown(f"<strong><span style='color:red;font-size:25px;'>以下即将进行AOE战斗模拟</span></strong>", unsafe_allow_html=True)

hudun_pd = st.checkbox("守方是否有护盾（有就勾选）")
if hudun_pd:
    hudun_value = st.text_input("护盾值为", "0")
    hudun_value = mb_shuru(hudun_value)
else:
    hudun_value = 0
hudun_value = round(hudun_value)

# 初始化剩余护盾值
hudun_sy_value = hudun_value

zhgs_pd = st.checkbox("是否有战后固伤（有就勾选）")
if zhgs_pd:
    zh_gs = st.text_input("战后固伤为", "0")
    zh_gs = mb_shuru(zh_gs)
else:
    zh_gs = 0
zh_gs = round(zh_gs)

st.write("  ")

st.markdown(f"<strong><span style='color:red;font-size:20px;'>实际AOE伤害为</span></strong>", unsafe_allow_html=True)

column7, column8, column9 = st.columns([1,0.1,1])
with column7:
    yxdyx_sfbj = st.checkbox("英雄打英雄 是否暴击")
    if yxdyx_sfbj:
        yxdyx_aoesj_sh = round(yxdyx_aoebj_sh, 2)
        st.markdown(f"##### 英雄打英雄伤害为 <strong><span style='color:orange;font-size:25px;'>{yxdyx_aoesj_sh}</span></strong>", unsafe_allow_html=True)
    else:
        yxdyx_aoesj_sh = round(yxdyx_aoe_sh, 2)
        st.markdown(f"##### 英雄打英雄伤害为 <strong><span style='color:green;font-size:25px;'>{yxdyx_aoesj_sh}</span></strong>", unsafe_allow_html=True)

with column9:
    yxdb_sfbj = st.checkbox("英雄打兵 是否暴击")
    if yxdb_sfbj:
        yxdb_aoesj_sh = round(yxdb_aoebj_sh, 2)
        st.markdown(f"##### 英雄打兵伤害为 <strong><span style='color:orange;font-size:25px;'>{yxdb_aoesj_sh}</span></strong>", unsafe_allow_html=True)
    else:
        yxdb_aoesj_sh = round(yxdb_aoe_sh, 2)
        st.markdown(f"##### 英雄打兵伤害为 <strong><span style='color:blue;font-size:25px;'>{yxdb_aoesj_sh}</span></strong>", unsafe_allow_html=True)

aoe_zsh = round(yxdyx_aoesj_sh) + round(yxdb_aoesj_sh)

st.markdown(f"##### 头上冒出的总伤害为（英雄+兵） <strong><span style='color:red;font-size:30px;'>{aoe_zsh}</span></strong>", unsafe_allow_html=True)

#初始化变量
zsh = aoe_zsh
yxdyx = round(yxdyx_aoesj_sh)
yxdb = round(yxdb_aoesj_sh)

st.write("  ")

if st.button("点击保存此段伤害"):
    hudun_sy_value = max(0,hudun_sy_value - sum(st.session_state.saved_hudun_cs_value))
    if zsh >= hudun_sy_value:
        if hudun_sy_value != 0:
            zsh_zz = zsh - hudun_sy_value
            hudun_cs_value = hudun_sy_value
            if zsh == 0:
                yxdyx_zz = 0
                yxdb_zz = 0
                hudun_yxdyx_cs_value = 0
                hudun_yxdb_cs_value = 0
            else:
                yxdyx_zz = round(zsh_zz * (yxdyx / zsh))
                yxdb_zz = round(zsh_zz * (yxdb / zsh))
                hudun_yxdyx_cs_value = round(hudun_cs_value*(yxdyx/zsh))
                hudun_yxdb_cs_value = round(hudun_cs_value*(yxdb/zsh))
        else:
            zsh_zz = zsh
            yxdyx_zz = yxdyx
            yxdb_zz = yxdb
            hudun_cs_value = 0
            hudun_yxdyx_cs_value = 0
            hudun_yxdb_cs_value = 0
    else:
        zsh_zz = 0
        yxdyx_zz = 0
        yxdb_zz = 0
        hudun_cs_value = zsh
        if zsh == 0:
            hudun_yxdyx_cs_value = 0
            hudun_yxdb_cs_value = 0
        else:
            hudun_yxdyx_cs_value = round(hudun_cs_value * (yxdyx / zsh))
            hudun_yxdb_cs_value = round(hudun_cs_value * (yxdb / zsh))
    # 储存计算结果
    st.session_state.saved_damage_yxdyx.append(yxdyx_zz) # 保存英雄打英雄伤害
    st.session_state.saved_damage_yxdb.append(yxdb_zz) # 保存英雄打兵伤害
    st.session_state.saved_damage_zsh.append(zsh_zz) # 保存总伤害
    st.session_state.saved_hudun_cs_value.append(hudun_cs_value) # 保存护盾承伤值（总伤害）
    st.session_state.saved_hudun_yxdyx_cs_value.append(hudun_yxdyx_cs_value) # 保存护盾承伤值（英雄打英雄）
    st.session_state.saved_hudun_yxdb_cs_value.append(hudun_yxdb_cs_value) # 保存护盾承伤值（英雄打兵）

# 分割线
st.divider()

column55, column56, column57 = st.columns([1,0.1,1])
with column55:
    if st.button("删除一段最新储存的伤害值"):
        if st.session_state.saved_damage_yxdyx:
            st.session_state.saved_damage_yxdyx.pop()
        if st.session_state.saved_damage_yxdb:
            st.session_state.saved_damage_yxdb.pop()
        if st.session_state.saved_damage_zsh:
            st.session_state.saved_damage_zsh.pop()
        if st.session_state.saved_hudun_cs_value:
            st.session_state.saved_hudun_cs_value.pop()
        if st.session_state.saved_hudun_yxdyx_cs_value:
            st.session_state.saved_hudun_yxdyx_cs_value.pop()
        if st.session_state.saved_hudun_yxdb_cs_value:
            st.session_state.saved_hudun_yxdb_cs_value.pop()
with column57:
    if st.button("清空所有储存的伤害值"):
        st.session_state.saved_damage_yxdyx = []
        st.session_state.saved_damage_yxdb = []
        st.session_state.saved_damage_zsh = []
        st.session_state.saved_hudun_cs_value = []
        st.session_state.saved_hudun_yxdyx_cs_value = []
        st.session_state.saved_hudun_yxdb_cs_value = []

st.write("  ")

#计算战后固伤
if hudun_value - sum(st.session_state.saved_hudun_cs_value) > 0 and zhgs_pd: #如果多段AOE打完后还有护盾
    hudun_sy_value_zh_gs = hudun_sy_value - sum(st.session_state.saved_hudun_cs_value) #打战后固伤前还剩余的护盾值
    if zh_gs*2 <= hudun_sy_value_zh_gs:
        zh_gs_yxdyx = 0
        zh_gs_yxdb = 0
        zh_gs_zsh = 0
        zh_gs_yxdyx_hudun_cs = zh_gs
        zh_gs_yxdb_hudun_cs = zh_gs
        zh_gs_zsh_hudun_cs = zh_gs*2
    else:
        zh_gs_yxdyx = round((zh_gs*2 - hudun_sy_value_zh_gs)/2)
        zh_gs_yxdb = round((zh_gs*2 - hudun_sy_value_zh_gs)/2)
        zh_gs_zsh = zh_gs_yxdyx + zh_gs_yxdb
        zh_gs_yxdyx_hudun_cs = hudun_sy_value_zh_gs/2
        zh_gs_yxdb_hudun_cs = hudun_sy_value_zh_gs/2
        zh_gs_zsh_hudun_cs = hudun_sy_value_zh_gs
else:
    zh_gs_yxdyx = zh_gs
    zh_gs_yxdb = zh_gs
    zh_gs_zsh = zh_gs*2
    zh_gs_zsh_hudun_cs = 0

column97, column98, column99 = st.columns([1,0.1,1])

with column97:
    st.markdown(f"<strong><span style='color:green;font-size:20px;'>英雄打英雄</span></strong>", unsafe_allow_html=True)
    # 显示英雄打英雄所有的伤害值
    for i, (damage_yxdyx, hudun_yxdyx_cs) in enumerate(zip(st.session_state.saved_damage_yxdyx,st.session_state.saved_hudun_yxdyx_cs_value), start=1):
        if hudun_yxdyx_cs != 0:
            st.write(f"(护盾)已抵挡第{i}段伤害 {hudun_yxdyx_cs}")
        st.write(f"第{i}段造成伤害值为 {damage_yxdyx}")
    if zhgs_pd:
        if hudun_value - sum(st.session_state.saved_hudun_cs_value) > 0:
            st.write(f"(护盾)已抵挡战后固伤 {zh_gs_yxdyx_hudun_cs}")
        st.write(f"战后固伤造成伤害值为: {zh_gs_yxdyx}")
    # 计算总伤害
    total_damage_yxdyx = sum(st.session_state.saved_damage_yxdyx)
    st.markdown(f"英雄打英雄总伤害（不含护盾）: <strong><span style='color:green;font-size:20px;'>{total_damage_yxdyx + zh_gs_yxdyx}</span></strong>", unsafe_allow_html=True)

with column99:
    st.markdown(f"<strong><span style='color:blue;font-size:20px;'>英雄打兵</span></strong>", unsafe_allow_html=True)
    # 显示英雄打兵所有的伤害值
    for j,  (damage_yxdb, hudun_yxdb_cs) in enumerate(zip(st.session_state.saved_damage_yxdb,st.session_state.saved_hudun_yxdb_cs_value), start=1):
        if hudun_yxdb_cs != 0:
            st.write(f"(护盾)已抵挡第{j}段伤害 {hudun_yxdb_cs}")
        st.write(f"第{j}段造成伤害值为 {damage_yxdb}")
    if zhgs_pd:
        if hudun_value - sum(st.session_state.saved_hudun_cs_value) > 0:
            st.write(f"(护盾)已抵挡战后固伤 {zh_gs_yxdb_hudun_cs}")
        st.write(f"战后固伤: {zh_gs_yxdb}")
    # 计算总伤害
    total_damage_yxdb = sum(st.session_state.saved_damage_yxdb)
    st.markdown(f"英雄打兵总伤害（不含护盾）: <strong><span style='color:blue;font-size:20px;'>{total_damage_yxdb + zh_gs_yxdb}</span></strong>", unsafe_allow_html=True)

st.write("")

st.markdown(f"<strong><span style='color:red;font-size:20px;'>总伤害打（英雄+兵）</span></strong>", unsafe_allow_html=True)
# 显示总伤害（英雄+兵）所有的伤害值
for k, (damage_zsh, hudun_zsh_cs) in enumerate(zip(st.session_state.saved_damage_zsh,st.session_state.saved_hudun_cs_value), start=1):
    if hudun_zsh_cs != 0:
        st.write(f"(护盾)已抵挡第{k}段伤害 {hudun_zsh_cs}")
    st.write(f"第{k}段造成伤害值为 {damage_zsh}")
if zhgs_pd:
    if hudun_value - sum(st.session_state.saved_hudun_cs_value) > 0:
        st.write(f"(护盾)已抵挡战后固伤 {zh_gs_zsh_hudun_cs}")
    st.write(f"战后固伤: {zh_gs_zsh}")
# 计算总伤害
total_damage_zsh = sum(st.session_state.saved_damage_zsh)
st.markdown(f"打（英雄+兵）总伤害（不含护盾）: <strong><span style='color:red;font-size:20px;'>{total_damage_zsh + zh_gs_zsh}</span></strong>", unsafe_allow_html=True)

st.write("")
if hudun_pd:
    if zhgs_pd:
        hudun_sy_value = max(0,hudun_value - sum(st.session_state.saved_hudun_cs_value) - zh_gs_zsh_hudun_cs)
    else:
        hudun_sy_value = max(0,hudun_value - sum(st.session_state.saved_hudun_cs_value))
    st.markdown(f"护盾剩余值: <strong><span style='color:orange;font-size:20px;'>{hudun_sy_value}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

text_shuoming = ("""使用说明：

（1）里面每个输入框都是可以直接用英文符号直接用公式计算的，如1588/1.2*(1+0.2+0.3)*1.4非常方便数值调整。

（2）增减伤、克制系数、无视克制都是默认百分比形式，如增伤应输入“20+5+8”，如克制系数如果是魔力震荡打圣职应输入“50”

（3）克制修正输入的开关在攻方处，如果需要输入守方的双防克制系数加成，需要在攻方区域打开克制关系。如守方有冰女王的彻骨寒意，可在守方双防克制修正填-20

（4）物理和魔法伤害需要手动选择，物理伤害默认用攻击-防御，魔法伤害默认用智力-魔防，如像雾香这类物理转魔法，应将雾香的攻击填到智力处，不然不能正常生效。

（5) 攻方暴击伤害已默认1.3，如果有额外暴伤只需要填入额外爆伤，如锋刺填10

（6) 考虑了英雄对英雄、英雄对士兵的分别计算，便于验证打本体是否暴击

（7）加了伤害保存功能，用户可保存每一段的AOE伤害进行合计，但在保存前，需要判断好暴击还是不暴击

（8）增加了“储存清零”和“只清上一段伤害功能

（9）增加了“战后固伤”的计算，战后固伤可以使用公式

（10）增加了护盾机制，使用护盾功能前（无论是关闭还是开启），请清空所有保存的段数，再重新保存，否则计算会出错。

（11）护盾默认要同步计算英雄对士兵的伤害，如果未填写守方士兵的数值，护盾计算会出错。

（12）如果敌方未携带士兵又有护盾，无需使用护盾功能，将护盾看成是敌方英雄的血量即可。

如有疑问加梦战计算器使用交流群 928411216""")

st.markdown(text_shuoming,unsafe_allow_html=True)