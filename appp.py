import math
import streamlit as st
import re

#定义面板输入函数
def mb_shuru(shuxing):
    if shuxing == "":
        shuxing = 0
    else:
        nums = re.findall(r"\d+", shuxing)
        nums = [int(num) for num in nums]
        shuxing = eval(shuxing)
    return shuxing

#定义百分比输入函数
def bfb_shuru(baifenbi):
    if baifenbi == "":
        baifenbi = 0
    else:
        # 计算某属性
        nums = re.findall(r"\d+", baifenbi)
        nums = [int(num) for num in nums]
        baifenbi = eval(baifenbi)*0.01
    return baifenbi

#标题
st.title('梦幻模拟战-单点模拟计算器')

column1, column2, column3 = st.columns([1,0.3,1])

with column1:
    st.write("### 攻方")
    tab1, tab2 = st.tabs(["士兵", "英雄"])
    with tab1:
        # 定义攻方士兵攻击
        gf_sbgj = st.text_input("攻方士兵攻击", "0")
        gf_sbgj = mb_shuru(gf_sbgj)
        column11, column12 = st.columns([1, 1])
        with column11:
            # 定义攻方士兵攻击克制系数
            gf_sb_gjkzxs = st.text_input("士兵攻击克制系数%", "0")
            gf_sb_gjkzxs = bfb_shuru(gf_sb_gjkzxs)
            # 选择物理还是魔法伤害
            sbsh_lx = st.radio("士兵伤害类型", ("物理", "魔法"))
        with column12:
            # 定义攻方士兵无视双防系数
            gf_sb_wsfy = st.text_input("士兵无视双防系数%", "0")
            gf_sb_wsfy = bfb_shuru(gf_sb_wsfy)
            # 定义攻方士兵技能倍率
            gf_sbjnbl = st.text_input("攻方士兵技能倍率", "1")
            gf_sbjnbl = mb_shuru(gf_sbjnbl)
        # 定义攻方士兵通用增伤
        gf_sb_tyzs = st.text_input("攻方士兵通用增伤%", "0")
        gf_sb_tyzs = bfb_shuru(gf_sb_tyzs)
        column13, column14 = st.columns([1, 1])
        with column13:
            # 定义攻方士兵技能增伤
            gf_sb_jnzs = st.text_input("攻方士兵技能增伤%", "0")
            gf_sb_jnzs = bfb_shuru(gf_sb_jnzs)
            # 定义攻方士兵其他增伤
            gf_sb_qtzs = st.text_input("攻方士兵其他增伤%", "0")
            gf_sb_qtzs = bfb_shuru(gf_sb_qtzs)
        with column14:
            # 定义攻方士兵远程增伤
            gf_sb_yczs = st.text_input("攻方士兵远程增伤%", "0")
            gf_sb_yczs = bfb_shuru(gf_sb_yczs)
            # 定义攻方士兵暴伤加成
            gf_sb_bs = st.text_input("攻方士兵暴伤加成%", "0")
            gf_sb_bs = bfb_shuru(gf_sb_bs)
    with tab2:
        # 定义攻方英雄攻击
        gf_yxgj = st.text_input("攻方英雄攻击", "0")
        gf_yxgj = mb_shuru(gf_yxgj)
        # 定义攻方英雄智力
        gf_yxzl = st.text_input("攻方英雄智力", "0")
        gf_yxzl = mb_shuru(gf_yxzl)
        column21, column22 = st.columns([1, 1])
        with column21:
            # 定义攻方英雄攻击克制系数
            gf_yx_gzkzxs = st.text_input("攻智克制系数%", "0")
            gf_yx_gzkzxs = bfb_shuru(gf_yx_gzkzxs)
            # 选择物理还是魔法伤害
            yxsh_lx = st.radio("英雄伤害类型", ("物理", "魔法"))
        with column22:
            # 定义攻方英雄无视双防系数
            gf_yx_wsfy = st.text_input("无视双防系数%", "0")
            gf_yx_wsfy = bfb_shuru(gf_yx_wsfy)
            # 定义攻方英雄技能倍率
            gf_yxjnbl = st.text_input("攻方英雄技能倍率", "1")
            gf_yxjnbl = mb_shuru(gf_yxjnbl)
        # 定义攻方英雄物理通用增伤
        gf_yx_tyzs = st.text_input("攻方英雄通用增伤%", "0")
        gf_yx_tyzs = bfb_shuru(gf_yx_tyzs)
        column23, column24 = st.columns([1, 1])
        with column23:
            # 定义攻方英雄技能增伤
            gf_yx_jnzs = st.text_input("攻方英雄技能增伤%", "0")
            gf_yx_jnzs = bfb_shuru(gf_yx_jnzs)
            # 定义攻方英雄其他增伤
            gf_yx_qtzs = st.text_input("攻方英雄其他增伤%", "0")
            gf_yx_qtzs = bfb_shuru(gf_yx_qtzs)
        with column24:
            # 定义攻方英雄远程增伤
            gf_yx_yczs = st.text_input("攻方英雄远程增伤%", "0")
            gf_yx_yczs = bfb_shuru(gf_yx_yczs)
            # 定义攻方英雄暴伤加成
            gf_yx_bs = st.text_input("攻方英雄暴伤加成%", "0")
            gf_yx_bs = bfb_shuru(gf_yx_bs)
        # 选择攻方英雄攻击段数是否为20段
        gf_yx_gjdspd = st.checkbox("攻方英雄攻击段数是否为20段", value=True)
        if gf_yx_gjdspd:
            gf_yx_gjds = 20  # 默认为20
        else:
            gf_yx_gjds = st.number_input("攻方英雄攻击段数", min_value=1, value=40)

with column3:
    st.write("### 守方")
    tab3, tab4 = st.tabs(["士兵", "英雄"])
    with tab3:
        column31, column32 = st.columns([1, 1])
        with column31:
            # 定义守方士兵防御
            sf_sbfy = st.text_input("守方士兵防御", "0")
            sf_sbfy = mb_shuru(sf_sbfy)
        with column32:
            # 定义守方士兵魔防
            sf_sbmf = st.text_input("守方士兵魔防", "0")
            sf_sbmf = mb_shuru(sf_sbmf)
        # 定义守方士兵双防克制系数
        sf_sb_sfkzxs = st.text_input("守方士兵双防克制系数%", "0")
        sf_sb_sfkzxs = bfb_shuru(sf_sb_sfkzxs)
        # 定义守方士兵物理通用减伤
        sf_sb_wl_tyjs = st.text_input("守方士兵物理通用减伤%", "0")
        sf_sb_wl_tyjs = bfb_shuru(sf_sb_wl_tyjs)
        # 定义守方士兵魔法通用减伤
        sf_sb_mf_tyjs = st.text_input("守方士兵魔法通用减伤%", "0")
        sf_sb_mf_tyjs = bfb_shuru(sf_sb_mf_tyjs)
        column33, column34 = st.columns([1, 1])
        with column33:
            # 定义守方士兵技能减伤
            sf_sb_jnjs = st.text_input("守方士兵技能减伤%", "0")
            sf_sb_jnjs = bfb_shuru(sf_sb_jnjs)
            # 定义守方士兵其他减伤
            sf_sb_qtjs = st.text_input("守方士兵其他减伤%", "0")
            sf_sb_qtjs = bfb_shuru(sf_sb_qtjs)
        with column34:
            # 定义守方士兵远程减伤
            sf_sb_ycjs = st.text_input("守方士兵远程减伤%", "0")
            sf_sb_ycjs = bfb_shuru(sf_sb_ycjs)
            # 定义守方士兵减暴伤
            sf_sb_jbs = st.text_input("守方士兵减暴伤%", "0")
            sf_sb_jbs = bfb_shuru(sf_sb_jbs)
    with tab4:
        # 定义守方英雄防御
        sf_yxfy = st.text_input("守方英雄防御", "0")
        sf_yxfy = mb_shuru(sf_yxfy)
        # 定义守方英雄魔防
        sf_yxmf = st.text_input("守方英雄魔防", "0")
        sf_yxmf = mb_shuru(sf_yxmf)
        # 定义守方英雄双防克制系数
        sf_yx_sfkzxs = st.text_input("守方英雄双防克制系数%", "0")
        sf_yx_sfkzxs = bfb_shuru(sf_yx_sfkzxs)
        # 定义守方英雄物理通用减伤
        sf_yx_wl_tyjs = st.text_input("守方英雄物理通用减伤%", "0")
        sf_yx_wl_tyjs = bfb_shuru(sf_yx_wl_tyjs)
        # 定义守方英雄魔法通用减伤
        sf_yx_mf_tyjs = st.text_input("守方英雄魔法通用减伤%", "0")
        sf_yx_mf_tyjs = bfb_shuru(sf_yx_mf_tyjs)
        column41, column42 = st.columns([1, 1])
        with column41:
            # 定义守方英雄技能减伤
            sf_yx_jnjs = st.text_input("守方英雄技能减伤%", "0")
            sf_yx_jnjs = bfb_shuru(sf_yx_jnjs)
            # 定义守方英雄其他减伤
            sf_yx_qtjs = st.text_input("守方英雄其他减伤%", "0")
            sf_yx_qtjs = bfb_shuru(sf_yx_qtjs)
        with column42:
            # 定义守方英雄远程减伤
            sf_yx_ycjs = st.text_input("守方英雄远程减伤%", "0")
            sf_yx_ycjs = bfb_shuru(sf_yx_ycjs)
            # 定义守方英雄减暴伤
            sf_yx_jbs = st.text_input("守方英雄减暴伤%", "0")
            sf_yx_jbs = bfb_shuru(sf_yx_jbs)

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

#分割线
st.divider()

#定义兵打兵单段伤害 bdb_dd_sh
#定义兵打兵单段暴击伤害 bdb_ddbj_sh
#定义兵打英雄单段伤害 bdyx_dd_sh
#定义兵打英雄单段暴击伤害 bdyx_ddbj_sh

if sbsh_lx == "物理":
#计算兵打兵物理伤害
    bdb_dd_sh = (gf_sbgj*(1+gf_sb_gjkzxs) - sf_sbfy*(1+sf_sb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs-sf_sb_wl_tyjs) * (1+gf_sb_jnzs-sf_sb_jnjs) * (1+gf_sb_yczs-sf_sb_ycjs) * (1+gf_sb_qtzs-sf_sb_qtjs) * 0.5
    bdb_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_sb_jbs)
#计算兵打英雄物理伤害
    bdyx_dd_sh = (gf_sbgj*(1+gf_sb_gjkzxs) - sf_yxfy*(1+sf_yx_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs- sf_yx_wl_tyjs) * (1+gf_sb_jnzs-sf_yx_jnjs) * (1+gf_sb_yczs-sf_yx_ycjs) * (1+gf_sb_qtzs-sf_yx_qtjs) * 0.5
    bdyx_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_yx_jbs)
else:
#计算兵打兵魔法伤害
    bdb_dd_sh = (gf_sbgj*(1+gf_sb_gjkzxs) - sf_sbmf*(1+sf_sb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs-sf_sb_mf_tyjs) * (1+gf_sb_jnzs-sf_sb_jnjs) * (1+gf_sb_yczs-sf_sb_ycjs) * (1+gf_sb_qtzs-sf_sb_qtjs) * 0.5
    bdb_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_sb_jbs)
#计算兵打英雄魔法伤害
    bdyx_dd_sh = (gf_sbgj*(1+gf_sb_gjkzxs) - sf_yxmf*(1+sf_yx_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs- sf_yx_mf_tyjs) * (1+gf_sb_jnzs-sf_yx_jnjs) * (1+gf_sb_yczs-sf_yx_ycjs) * (1+gf_sb_qtzs-sf_yx_qtjs) * 0.5
    bdyx_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_yx_jbs)

#定义英雄打兵单段伤害 yxdb_dd_sh
#定义英雄打兵单段暴击伤害 yxdb_ddbj_sh
#定义英雄打英雄单段伤害 yxdyx_dd_sh
#定义英雄打英雄单段暴击伤害 yxdyx_ddbj_sh

if yxsh_lx == "物理":
#计算英雄打兵物理伤害
    yxdb_dd_sh = (gf_yxgj*(1+gf_yx_gzkzxs) - sf_sbfy*(1+sf_sb_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_wl_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 0.5
    yxdb_ddbj_sh = yxdb_dd_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄物理伤害
    yxdyx_dd_sh = (gf_yxgj*(1+gf_yx_gzkzxs) - sf_yxfy*(1+sf_yx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_wl_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 0.5
    yxdyx_ddbj_sh = yxdyx_dd_sh * (1.3+gf_yx_bs-sf_yx_jbs)
else:
#计算英雄打兵魔法伤害
    yxdb_dd_sh = (gf_yxzl*(1+gf_yx_gzkzxs) - sf_sbmf*(1+sf_sb_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_mf_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 0.5
    yxdb_ddbj_sh = yxdb_dd_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄魔法伤害
    yxdyx_dd_sh = (gf_yxzl*(1+gf_yx_gzkzxs) - sf_yxmf*(1+sf_yx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_mf_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 0.5
    yxdyx_ddbj_sh = yxdyx_dd_sh * (1.3+gf_yx_bs-sf_yx_jbs)

column4, column5, column6 = st.columns([1,0.1,1])

with column4:
    st.markdown(f"##### 兵打兵单段伤害为 <strong><span style='color:blue;font-size:25px;'>{bdb_dd_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 兵打兵暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{bdb_ddbj_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打兵单段伤害为 <strong><span style='color:blue;font-size:25px;'>{yxdb_dd_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打兵暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{yxdb_ddbj_sh}</span></strong>", unsafe_allow_html=True)

with column6:
    st.markdown(f"##### 兵打英雄单段伤害为 <strong><span style='color:green;font-size:25px;'>{bdyx_dd_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 兵打英雄暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{bdyx_ddbj_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打英雄单段伤害为 <strong><span style='color:green;font-size:25px;'>{yxdyx_dd_sh}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打英雄暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{yxdyx_ddbj_sh}</span></strong>", unsafe_allow_html=True)

#分割线
st.divider()
#判断是否暴击
bdb_sfbj = st.checkbox("兵打兵 是否暴击")
bdyx_sfbj = st.checkbox("兵打英雄 是否暴击")
yxdb_sfbj = st.checkbox("英雄打兵 是否暴击")
yxdyx_sfbj = st.checkbox("英雄打英雄 是否暴击")

if bdb_sfbj:
    sj_bdb_sh = round(bdb_ddbj_sh)
else:
    sj_bdb_sh = round(bdb_dd_sh)

if bdb_sfbj:
    sj_bdyx_sh = round(bdyx_ddbj_sh)
else:
    sj_bdyx_sh = round(bdyx_dd_sh)

if yxdb_sfbj:
    sj_yxdb_sh = round(yxdb_ddbj_sh)
else:
    sj_yxdb_sh = round(yxdb_dd_sh)

if yxdyx_sfbj:
    sj_yxdyx_sh = round(yxdyx_ddbj_sh)
else:
    sj_yxdyx_sh = round(yxdyx_dd_sh)

if sj_bdb_sh < 1:
    sj_bdb_sh = 1
if sj_bdyx_sh < 1:
    sj_bdyx_sh = 1
if sj_yxdb_sh < 1:
    sj_yxdb_sh = 1
if sj_yxdyx_sh < 1:
    sj_yxdyx_sh = 1

#分割线
st.divider()

# 攻方士兵是否满血选择
attacker_full_health = st.checkbox("攻方士兵是否满血",value=True)

if attacker_full_health:
    attacker_soldier_count = 10  # 满血时固定为10
    st.write("攻方士兵当前数量: 10（满血）")
else:
    attacker_soldier_count = st.number_input("攻方士兵当前数量", min_value=0, value=10)  # 不满血时用户可以输入数量

#分割线
st.divider()

# 守方士兵的最大血量输入
defender_soldier_max_hp_per_unit = st.number_input("每只守方士兵的最大血量", min_value=1, value=1)

# 守方士兵是否满血选择
defender_full_health = st.checkbox("守方士兵是否满血",value=True)

if defender_full_health:
    defender_soldier_count = 10  # 满血时固定为10
    defender_soldier_hp = defender_soldier_max_hp_per_unit * 10  # 总血量为最大血量 * 10
    st.write(f"守方士兵当前总血量: {defender_soldier_hp}（满血）")
else:
    defender_soldier_hp = st.text_input("守方士兵当前总血量", "0") # 不满血时用户可以输入总血量
    if defender_soldier_hp == "":
        defender_soldier_hp = 0
    else:
        # 计算守方英雄当前血量
        nums = re.findall(r"\d+", defender_soldier_hp)
        nums = [int(num) for num in nums]
        defender_soldier_hp = eval(defender_soldier_hp)
    # 守方英雄当前血量最小为1
    if defender_soldier_hp <= 0:
        defender_soldier_hp = 0
    defender_soldier_count = math.ceil(defender_soldier_hp / defender_soldier_max_hp_per_unit)  # 计算守方士兵数量

#分割线
st.divider()

#定义守方英雄当前血量
defender_hero_hp = st.text_input("守方英雄当前血量","1")
if defender_hero_hp == "":
    defender_hero_hp= 0
else:
#计算守方英雄当前血量
    nums = re.findall(r"\d+", defender_hero_hp )
    nums = [int(num) for num in nums]
    defender_hero_hp = eval(defender_hero_hp)
#守方英雄当前血量最小为1
if defender_hero_hp <=1:
    defender_hero_hp = 1

#分割线
st.divider()

sdsr_pd = st.checkbox("读取以上单段伤害计算结果，不手动输入单段伤害", value=True)

if sdsr_pd:
    soldier_to_soldier_damage = sj_bdb_sh
    soldier_to_hero_damage = sj_bdyx_sh
    hero_to_soldier_damage = sj_yxdb_sh
    hero_to_hero_damage = sj_yxdyx_sh
else:
    soldier_to_soldier_damage = st.number_input("士兵打士兵的单段伤害", min_value=1,value=1)
    soldier_to_hero_damage = st.number_input("士兵打英雄的单段伤害", min_value=1,value=1)
    hero_to_soldier_damage = st.number_input("英雄打士兵的单段伤害", min_value=1,value=1)
    hero_to_hero_damage = st.number_input("英雄打英雄的单段伤害", min_value=1,value=1)

#分割线
st.divider()

# 士兵出手的最大段数（按攻方士兵数量和每只士兵的2段攻击计算）
attacker_soldier_max_segments = attacker_soldier_count * 2

# 用户选择士兵优先出手的段数
st.write(f"士兵出手的段数最大参考值: {attacker_soldier_max_segments}")
if attacker_soldier_count == 0:
    soldier_to_soldier_priority_segments = 0
else:
    soldier_to_soldier_priority_segments = st.slider("请选择士兵优先英雄出手的段数（根据英雄出手速度判断）", min_value=0, max_value=attacker_soldier_max_segments, value=attacker_soldier_max_segments)

# 初始化剩余士兵段数、英雄出手段数
remaining_soldier_segments = attacker_soldier_max_segments - soldier_to_soldier_priority_segments
hero_segments = gf_yx_gjds

# 初始化守方士兵和英雄的剩余血量
defender_soldier_remaining_hp = defender_soldier_hp
defender_hero_remaining_hp = defender_hero_hp

# 处理士兵优先出手段数，逐个计算守方士兵承伤
soldier_to_soldier_segments_used = 0
for i in range(defender_soldier_count):
    current_soldier_hp = min(defender_soldier_max_hp_per_unit, defender_soldier_remaining_hp)

    # 计算当前士兵能承受的段数
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / soldier_to_soldier_damage)

    if soldier_to_soldier_priority_segments >= segments_needed_to_kill_soldier:
        # 杀死当前士兵
        soldier_to_soldier_priority_segments -= segments_needed_to_kill_soldier
        defender_soldier_remaining_hp -= current_soldier_hp
        soldier_to_soldier_segments_used += segments_needed_to_kill_soldier
    else:
        # 当前士兵未被打死
        defender_soldier_remaining_hp -= soldier_to_soldier_priority_segments * soldier_to_soldier_damage
        soldier_to_soldier_segments_used += soldier_to_soldier_priority_segments
        soldier_to_soldier_priority_segments = 0
        break  # 没有剩余段数，跳出循环

# 若士兵段数还有剩余且守方士兵已被打光，则剩余段数打英雄
soldier_to_hero_segments = soldier_to_soldier_priority_segments

# 英雄出手段数，逐个计算剩余守方士兵承伤
hero_to_soldier_segments_used = 0
for i in range(defender_soldier_count):
    if defender_soldier_remaining_hp <= 0:
        break

    current_soldier_hp = min(defender_soldier_max_hp_per_unit, defender_soldier_remaining_hp)
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / hero_to_soldier_damage)

    if hero_segments >= segments_needed_to_kill_soldier:
        # 杀死当前士兵
        hero_segments -= segments_needed_to_kill_soldier
        defender_soldier_remaining_hp -= current_soldier_hp
        hero_to_soldier_segments_used += segments_needed_to_kill_soldier
    else:
        # 当前士兵未被打死
        defender_soldier_remaining_hp -= hero_segments * hero_to_soldier_damage
        hero_to_soldier_segments_used += hero_segments
        hero_segments = 0
        break  # 没有剩余段数，跳出循环

# 若英雄出手段数还有剩余且守方士兵已被打光，则剩余段数打英雄
hero_to_hero_segments = hero_segments

# 处理剩余士兵段数，逐个计算剩余守方士兵承伤
remaining_soldier_to_soldier_segments_used = 0
for i in range(defender_soldier_count):
    if defender_soldier_remaining_hp <= 0:
        break

    current_soldier_hp = min(defender_soldier_max_hp_per_unit, defender_soldier_remaining_hp)
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / soldier_to_soldier_damage)

    if remaining_soldier_segments >= segments_needed_to_kill_soldier:
        # 杀死当前士兵
        remaining_soldier_segments -= segments_needed_to_kill_soldier
        defender_soldier_remaining_hp -= current_soldier_hp
        remaining_soldier_to_soldier_segments_used += segments_needed_to_kill_soldier
    else:
        # 当前士兵未被打死
        defender_soldier_remaining_hp -= remaining_soldier_segments * soldier_to_soldier_damage
        remaining_soldier_to_soldier_segments_used += remaining_soldier_segments
        remaining_soldier_segments = 0
        break  # 没有剩余段数，跳出循环

# 若士兵后续段数还有剩余且守方士兵已被打光，则剩余段数打英雄
remaining_soldier_to_hero_segments = remaining_soldier_segments

# 计算守方英雄的剩余血量
defender_hero_remaining_hp = max(0, defender_hero_remaining_hp - soldier_to_hero_segments * soldier_to_hero_damage - hero_to_hero_segments * hero_to_hero_damage - remaining_soldier_to_hero_segments * soldier_to_hero_damage)

# 输出战斗段数信息
# 士兵优先出手打士兵的实际段数: soldier_to_soldier_segments_used
# 士兵打英雄的段数: soldier_to_hero_segments
# 英雄打士兵的段数: hero_to_soldier_segments_used
# 英雄打英雄的段数: hero_to_hero_segments
# 士兵后续打士兵的实际段数: remaining_soldier_to_soldier_segments_used
# 士兵后续打英雄的段数: remaining_soldier_to_hero_segments

column91, column92, column93 = st.columns([1,0.1,1])
with column91:
    st.write(f"士兵打士兵的段数: {soldier_to_soldier_segments_used + remaining_soldier_to_soldier_segments_used} ")
    st.write(f"士兵打英雄的段数: {soldier_to_hero_segments + remaining_soldier_to_hero_segments} ")
    st.write(f"英雄打士兵的段数: {hero_to_soldier_segments_used} ")
    st.write(f"英雄打英雄的段数: {hero_to_hero_segments} ")
with column93:
    st.write(f"士兵打士兵伤害: {(soldier_to_soldier_segments_used + remaining_soldier_to_soldier_segments_used) * soldier_to_soldier_damage}")
    st.write(f"士兵打英雄伤害: {(soldier_to_hero_segments + remaining_soldier_to_hero_segments) * soldier_to_hero_damage}")
    st.write(f"英雄打士兵伤害:{hero_to_soldier_segments_used * hero_to_soldier_damage}")
    st.write(f"英雄打英雄伤害: {hero_to_hero_segments * hero_to_hero_damage}")

# 分割线
st.divider()

# 输出守方士兵和英雄的剩余血量
st.markdown(f"##### 守方士兵剩余血量 <strong><span style='color:red;font-size:25px;'>{defender_soldier_remaining_hp}/{defender_soldier_hp}</span></strong>", unsafe_allow_html=True)
st.markdown(f"##### 守方英雄剩余血量 <strong><span style='color:green;font-size:25px;'>{defender_hero_remaining_hp}/{defender_hero_hp}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

# 定义本次单点总伤害
dd_zsh = (soldier_to_soldier_damage * soldier_to_soldier_segments_used +
          soldier_to_hero_damage * soldier_to_hero_segments +
          hero_to_soldier_damage * hero_to_soldier_segments_used +
          hero_to_hero_damage * hero_to_hero_segments +
          soldier_to_soldier_damage * remaining_soldier_to_soldier_segments_used +
          soldier_to_hero_damage * remaining_soldier_to_hero_segments)

dd_dsb_sh = (soldier_to_soldier_segments_used + remaining_soldier_to_soldier_segments_used)*soldier_to_soldier_damage + hero_to_soldier_segments_used*hero_to_soldier_damage
dd_dyx_sh = (soldier_to_hero_segments + remaining_soldier_to_hero_segments)*soldier_to_hero_damage + hero_to_hero_segments*hero_to_hero_damage

st.markdown(f"##### 本次单点总伤害 <strong><span style='color:blue;font-size:25px;'>{dd_zsh}</span></strong>", unsafe_allow_html=True)

st.markdown(f"###### 其中：对士兵造成伤害 <strong><span style='color:gray;font-size:20px;'>{dd_dsb_sh}</span></strong>", unsafe_allow_html=True)
st.markdown(f"###### 其中：对英雄造成伤害 <strong><span style='color:gray;font-size:20px;'>{dd_dyx_sh}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

st.write("目前计算器仍在测试中，梦战计算器使用交流群 928411216")
