\* Stac_MILP *\
Minimize
OBJ: 50 g_0_A + 50 g_0_B + 50 g_1_A + 50 g_1_B + 50 g_2_A + 50 g_2_B
 + 50 g_3_A + 50 g_3_B + 50 g_4_A + 50 g_4_B
Subject To
c01_sumT_0k0: T_(0,_0,_0) + T_(1,_0,_0) + T_(2,_0,_0) + T_(3,_0,_0)
 + T_(4,_0,_0) = 1
c01_sumT_0k1: T_(0,_0,_1) + T_(1,_0,_1) + T_(2,_0,_1) + T_(3,_0,_1)
 + T_(_1,_0,_1) = 1
c01_sumT_0k2: T_(0,_0,_2) + T_(1,_0,_2) + T_(2,_0,_2) + T_(_1,_0,_2)
 + T_(_2,_0,_2) = 1
c01_sumT_0k3: T_(0,_0,_3) + T_(1,_0,_3) + T_(_1,_0,_3) + T_(_2,_0,_3)
 + T_(_3,_0,_3) = 1
c01_sumT_0k4: T_(0,_0,_4) + T_(_1,_0,_4) + T_(_2,_0,_4) + T_(_3,_0,_4)
 + T_(_4,_0,_4) = 1
c01_sumT_1k0: T_(0,_1,_0) + T_(1,_1,_0) + T_(2,_1,_0) + T_(3,_1,_0)
 + T_(4,_1,_0) = 1
c01_sumT_1k1: T_(0,_1,_1) + T_(1,_1,_1) + T_(2,_1,_1) + T_(3,_1,_1)
 + T_(_1,_1,_1) = 1
c01_sumT_1k2: T_(0,_1,_2) + T_(1,_1,_2) + T_(2,_1,_2) + T_(_1,_1,_2)
 + T_(_2,_1,_2) = 1
c01_sumT_1k3: T_(0,_1,_3) + T_(1,_1,_3) + T_(_1,_1,_3) + T_(_2,_1,_3)
 + T_(_3,_1,_3) = 1
c01_sumT_1k4: T_(0,_1,_4) + T_(_1,_1,_4) + T_(_2,_1,_4) + T_(_3,_1,_4)
 + T_(_4,_1,_4) = 1
c01_sumT_2k0: T_(0,_2,_0) + T_(1,_2,_0) + T_(2,_2,_0) + T_(3,_2,_0)
 + T_(4,_2,_0) = 1
c01_sumT_2k1: T_(0,_2,_1) + T_(1,_2,_1) + T_(2,_2,_1) + T_(3,_2,_1)
 + T_(_1,_2,_1) = 1
c01_sumT_2k2: T_(0,_2,_2) + T_(1,_2,_2) + T_(2,_2,_2) + T_(_1,_2,_2)
 + T_(_2,_2,_2) = 1
c01_sumT_2k3: T_(0,_2,_3) + T_(1,_2,_3) + T_(_1,_2,_3) + T_(_2,_2,_3)
 + T_(_3,_2,_3) = 1
c01_sumT_2k4: T_(0,_2,_4) + T_(_1,_2,_4) + T_(_2,_2,_4) + T_(_3,_2,_4)
 + T_(_4,_2,_4) = 1
c02_Tposk0: T_(1,_0,_0) + T_(2,_0,_0) + T_(3,_0,_0) + T_(4,_0,_0) = 1
c02_Tposk1: T_(1,_0,_1) + T_(2,_0,_1) + T_(3,_0,_1) = 1
c02_Tposk2: T_(1,_0,_2) + T_(2,_0,_2) = 1
c02_Tposk3: T_(1,_0,_3) = 1
c02_Tposk4: T_(0,_0,_4) = 1
c03_Tnegk0: T_(0,_2,_0) = 1
c03_Tnegk1: T_(_1,_2,_1) = 1
c03_Tnegk2: T_(_1,_2,_2) + T_(_2,_2,_2) = 1
c03_Tnegk3: T_(_1,_2,_3) + T_(_2,_2,_3) + T_(_3,_2,_3) = 1
c03_Tnegk4: T_(_1,_2,_4) + T_(_2,_2,_4) + T_(_3,_2,_4) + T_(_4,_2,_4) = 1
c04_TRdecr_j0_m0k0: - T_(0,_1,_0) + T_(1,_0,_0) + T_(2,_0,_0) + T_(3,_0,_0)
 + T_(4,_0,_0) >= 0
c04_TRdecr_j0_m0k1: - T_(0,_1,_1) + T_(1,_0,_1) + T_(2,_0,_1) + T_(3,_0,_1)
 >= 0
c04_TRdecr_j0_m0k2: - T_(0,_1,_2) + T_(1,_0,_2) + T_(2,_0,_2) >= 0
c04_TRdecr_j0_m0k3: - T_(0,_1,_3) + T_(1,_0,_3) >= 0
c04_TRdecr_j0_m0k4: - T_(0,_1,_4) >= 0
c04_TRdecr_j0_m1k0: - T_(0,_2,_0) + T_(1,_1,_0) + T_(2,_1,_0) + T_(3,_1,_0)
 + T_(4,_1,_0) >= 0
c04_TRdecr_j0_m1k1: - T_(0,_2,_1) + T_(1,_1,_1) + T_(2,_1,_1) + T_(3,_1,_1)
 >= 0
c04_TRdecr_j0_m1k2: - T_(0,_2,_2) + T_(1,_1,_2) + T_(2,_1,_2) >= 0
c04_TRdecr_j0_m1k3: - T_(0,_2,_3) + T_(1,_1,_3) >= 0
c04_TRdecr_j0_m1k4: - T_(0,_2,_4) >= 0
c04_TRdecr_j1_m0k0: - T_(1,_1,_0) + T_(2,_0,_0) + T_(3,_0,_0) + T_(4,_0,_0)
 >= 0
c04_TRdecr_j1_m0k1: - T_(1,_1,_1) + T_(2,_0,_1) + T_(3,_0,_1) >= 0
c04_TRdecr_j1_m0k2: - T_(1,_1,_2) + T_(2,_0,_2) >= 0
c04_TRdecr_j1_m0k3: - T_(1,_1,_3) >= 0
c04_TRdecr_j1_m1k0: - T_(1,_2,_0) + T_(2,_1,_0) + T_(3,_1,_0) + T_(4,_1,_0)
 >= 0
c04_TRdecr_j1_m1k1: - T_(1,_2,_1) + T_(2,_1,_1) + T_(3,_1,_1) >= 0
c04_TRdecr_j1_m1k2: - T_(1,_2,_2) + T_(2,_1,_2) >= 0
c04_TRdecr_j1_m1k3: - T_(1,_2,_3) >= 0
c04_TRdecr_j2_m0k0: - T_(2,_1,_0) + T_(3,_0,_0) + T_(4,_0,_0) >= 0
c04_TRdecr_j2_m0k1: - T_(2,_1,_1) + T_(3,_0,_1) >= 0
c04_TRdecr_j2_m0k2: - T_(2,_1,_2) >= 0
c04_TRdecr_j2_m1k0: - T_(2,_2,_0) + T_(3,_1,_0) + T_(4,_1,_0) >= 0
c04_TRdecr_j2_m1k1: - T_(2,_2,_1) + T_(3,_1,_1) >= 0
c04_TRdecr_j2_m1k2: - T_(2,_2,_2) >= 0
c04_TRdecr_j3_m0k0: - T_(3,_1,_0) + T_(4,_0,_0) >= 0
c04_TRdecr_j3_m0k1: - T_(3,_1,_1) >= 0
c04_TRdecr_j3_m1k0: - T_(3,_2,_0) + T_(4,_1,_0) >= 0
c04_TRdecr_j3_m1k1: - T_(3,_2,_1) >= 0
c04_TRdecr_j4_m0k0: - T_(4,_1,_0) >= 0
c04_TRdecr_j4_m1k0: - T_(4,_2,_0) >= 0
c04_TRdecr_j_1_m0k1: T_(0,_0,_1) + T_(1,_0,_1) + T_(2,_0,_1) + T_(3,_0,_1)
 - T_(_1,_1,_1) >= 0
c04_TRdecr_j_1_m0k2: T_(0,_0,_2) + T_(1,_0,_2) + T_(2,_0,_2) - T_(_1,_1,_2)
 >= 0
c04_TRdecr_j_1_m0k3: T_(0,_0,_3) + T_(1,_0,_3) - T_(_1,_1,_3) >= 0
c04_TRdecr_j_1_m0k4: T_(0,_0,_4) - T_(_1,_1,_4) >= 0
c04_TRdecr_j_1_m1k1: T_(0,_1,_1) + T_(1,_1,_1) + T_(2,_1,_1) + T_(3,_1,_1)
 - T_(_1,_2,_1) >= 0
c04_TRdecr_j_1_m1k2: T_(0,_1,_2) + T_(1,_1,_2) + T_(2,_1,_2) - T_(_1,_2,_2)
 >= 0
c04_TRdecr_j_1_m1k3: T_(0,_1,_3) + T_(1,_1,_3) - T_(_1,_2,_3) >= 0
c04_TRdecr_j_1_m1k4: T_(0,_1,_4) - T_(_1,_2,_4) >= 0
c04_TRdecr_j_2_m0k2: T_(0,_0,_2) + T_(1,_0,_2) + T_(2,_0,_2) + T_(_1,_0,_2)
 - T_(_2,_1,_2) >= 0
c04_TRdecr_j_2_m0k3: T_(0,_0,_3) + T_(1,_0,_3) + T_(_1,_0,_3) - T_(_2,_1,_3)
 >= 0
c04_TRdecr_j_2_m0k4: T_(0,_0,_4) + T_(_1,_0,_4) - T_(_2,_1,_4) >= 0
c04_TRdecr_j_2_m1k2: T_(0,_1,_2) + T_(1,_1,_2) + T_(2,_1,_2) + T_(_1,_1,_2)
 - T_(_2,_2,_2) >= 0
c04_TRdecr_j_2_m1k3: T_(0,_1,_3) + T_(1,_1,_3) + T_(_1,_1,_3) - T_(_2,_2,_3)
 >= 0
c04_TRdecr_j_2_m1k4: T_(0,_1,_4) + T_(_1,_1,_4) - T_(_2,_2,_4) >= 0
c04_TRdecr_j_3_m0k3: T_(0,_0,_3) + T_(1,_0,_3) + T_(_1,_0,_3) + T_(_2,_0,_3)
 - T_(_3,_1,_3) >= 0
c04_TRdecr_j_3_m0k4: T_(0,_0,_4) + T_(_1,_0,_4) + T_(_2,_0,_4) - T_(_3,_1,_4)
 >= 0
c04_TRdecr_j_3_m1k3: T_(0,_1,_3) + T_(1,_1,_3) + T_(_1,_1,_3) + T_(_2,_1,_3)
 - T_(_3,_2,_3) >= 0
c04_TRdecr_j_3_m1k4: T_(0,_1,_4) + T_(_1,_1,_4) + T_(_2,_1,_4) - T_(_3,_2,_4)
 >= 0
c04_TRdecr_j_4_m0k4: T_(0,_0,_4) + T_(_1,_0,_4) + T_(_2,_0,_4) + T_(_3,_0,_4)
 - T_(_4,_1,_4) >= 0
c04_TRdecr_j_4_m1k4: T_(0,_1,_4) + T_(_1,_1,_4) + T_(_2,_1,_4) + T_(_3,_1,_4)
 - T_(_4,_2,_4) >= 0
c05_sumC_iA: c_0_A + c_1_A + c_2_A + c_3_A + c_4_A = 50
c05_sumC_iB: c_0_B + c_1_B + c_2_B + c_3_B + c_4_B = 50
c06_d_k0_j0_m0_iA: - 50 T_(0,_0,_0) - 0.990049833749 c_0_A + d_(0,_0,_0,_'A')
 >= -50
c06_d_k0_j0_m0_iB: - 50 T_(0,_0,_0) - 0.980198673307 c_0_B + d_(0,_0,_0,_'B')
 >= -50
c06_d_k0_j0_m1_iA: - 50 T_(0,_1,_0) - 0.00990049833749 c_0_A
 + d_(0,_0,_1,_'A') >= -50
c06_d_k0_j0_m1_iB: - 50 T_(0,_1,_0) - 0.0196039734661 c_0_B + d_(0,_0,_1,_'B')
 >= -50
c06_d_k0_j0_m2_iA: - 50 T_(0,_2,_0) - 4.96679133402e-05 c_0_A
 + d_(0,_0,_2,_'A') >= -50
c06_d_k0_j0_m2_iB: - 50 T_(0,_2,_0) - 0.00019735322711 c_0_B
 + d_(0,_0,_2,_'B') >= -50
c06_d_k0_j1_m0_iA: - 50 T_(1,_0,_0) - 0.990049833749 c_0_A + d_(0,_1,_0,_'A')
 >= -50
c06_d_k0_j1_m0_iB: - 50 T_(1,_0,_0) - 0.980198673307 c_0_B + d_(0,_1,_0,_'B')
 >= -50
c06_d_k0_j1_m1_iA: - 50 T_(1,_1,_0) - 0.00990049833749 c_0_A
 + d_(0,_1,_1,_'A') >= -50
c06_d_k0_j1_m1_iB: - 50 T_(1,_1,_0) - 0.0196039734661 c_0_B + d_(0,_1,_1,_'B')
 >= -50
c06_d_k0_j1_m2_iA: - 50 T_(1,_2,_0) - 4.96679133402e-05 c_0_A
 + d_(0,_1,_2,_'A') >= -50
c06_d_k0_j1_m2_iB: - 50 T_(1,_2,_0) - 0.00019735322711 c_0_B
 + d_(0,_1,_2,_'B') >= -50
c06_d_k0_j2_m0_iA: - 50 T_(2,_0,_0) - 0.990049833749 c_0_A + d_(0,_2,_0,_'A')
 >= -50
c06_d_k0_j2_m0_iB: - 50 T_(2,_0,_0) - 0.980198673307 c_0_B + d_(0,_2,_0,_'B')
 >= -50
c06_d_k0_j2_m1_iA: - 50 T_(2,_1,_0) - 0.00990049833749 c_0_A
 + d_(0,_2,_1,_'A') >= -50
c06_d_k0_j2_m1_iB: - 50 T_(2,_1,_0) - 0.0196039734661 c_0_B + d_(0,_2,_1,_'B')
 >= -50
c06_d_k0_j2_m2_iA: - 50 T_(2,_2,_0) - 4.96679133402e-05 c_0_A
 + d_(0,_2,_2,_'A') >= -50
c06_d_k0_j2_m2_iB: - 50 T_(2,_2,_0) - 0.00019735322711 c_0_B
 + d_(0,_2,_2,_'B') >= -50
c06_d_k0_j3_m0_iA: - 50 T_(3,_0,_0) - 0.990049833749 c_0_A + d_(0,_3,_0,_'A')
 >= -50
c06_d_k0_j3_m0_iB: - 50 T_(3,_0,_0) - 0.980198673307 c_0_B + d_(0,_3,_0,_'B')
 >= -50
c06_d_k0_j3_m1_iA: - 50 T_(3,_1,_0) - 0.00990049833749 c_0_A
 + d_(0,_3,_1,_'A') >= -50
c06_d_k0_j3_m1_iB: - 50 T_(3,_1,_0) - 0.0196039734661 c_0_B + d_(0,_3,_1,_'B')
 >= -50
c06_d_k0_j3_m2_iA: - 50 T_(3,_2,_0) - 4.96679133402e-05 c_0_A
 + d_(0,_3,_2,_'A') >= -50
c06_d_k0_j3_m2_iB: - 50 T_(3,_2,_0) - 0.00019735322711 c_0_B
 + d_(0,_3,_2,_'B') >= -50
c06_d_k0_j4_m0_iA: - 50 T_(4,_0,_0) - 0.990049833749 c_0_A + d_(0,_4,_0,_'A')
 >= -50
c06_d_k0_j4_m0_iB: - 50 T_(4,_0,_0) - 0.980198673307 c_0_B + d_(0,_4,_0,_'B')
 >= -50
c06_d_k0_j4_m1_iA: - 50 T_(4,_1,_0) - 0.00990049833749 c_0_A
 + d_(0,_4,_1,_'A') >= -50
c06_d_k0_j4_m1_iB: - 50 T_(4,_1,_0) - 0.0196039734661 c_0_B + d_(0,_4,_1,_'B')
 >= -50
c06_d_k0_j4_m2_iA: - 50 T_(4,_2,_0) - 4.96679133402e-05 c_0_A
 + d_(0,_4,_2,_'A') >= -50
c06_d_k0_j4_m2_iB: - 50 T_(4,_2,_0) - 0.00019735322711 c_0_B
 + d_(0,_4,_2,_'B') >= -50
c06_d_k1_j0_m0_iA: - 50 T_(0,_0,_1) - 0.990049833749 c_1_A + d_(1,_0,_0,_'A')
 >= -50
c06_d_k1_j0_m0_iB: - 50 T_(0,_0,_1) - 0.980198673307 c_1_B + d_(1,_0,_0,_'B')
 >= -50
c06_d_k1_j0_m1_iA: - 50 T_(0,_1,_1) - 0.00990049833749 c_1_A
 + d_(1,_0,_1,_'A') >= -50
c06_d_k1_j0_m1_iB: - 50 T_(0,_1,_1) - 0.0196039734661 c_1_B + d_(1,_0,_1,_'B')
 >= -50
c06_d_k1_j0_m2_iA: - 50 T_(0,_2,_1) - 4.96679133402e-05 c_1_A
 + d_(1,_0,_2,_'A') >= -50
c06_d_k1_j0_m2_iB: - 50 T_(0,_2,_1) - 0.00019735322711 c_1_B
 + d_(1,_0,_2,_'B') >= -50
c06_d_k1_j1_m0_iA: - 50 T_(1,_0,_1) - 0.990049833749 c_1_A + d_(1,_1,_0,_'A')
 >= -50
c06_d_k1_j1_m0_iB: - 50 T_(1,_0,_1) - 0.980198673307 c_1_B + d_(1,_1,_0,_'B')
 >= -50
c06_d_k1_j1_m1_iA: - 50 T_(1,_1,_1) - 0.00990049833749 c_1_A
 + d_(1,_1,_1,_'A') >= -50
c06_d_k1_j1_m1_iB: - 50 T_(1,_1,_1) - 0.0196039734661 c_1_B + d_(1,_1,_1,_'B')
 >= -50
c06_d_k1_j1_m2_iA: - 50 T_(1,_2,_1) - 4.96679133402e-05 c_1_A
 + d_(1,_1,_2,_'A') >= -50
c06_d_k1_j1_m2_iB: - 50 T_(1,_2,_1) - 0.00019735322711 c_1_B
 + d_(1,_1,_2,_'B') >= -50
c06_d_k1_j2_m0_iA: - 50 T_(2,_0,_1) - 0.990049833749 c_1_A + d_(1,_2,_0,_'A')
 >= -50
c06_d_k1_j2_m0_iB: - 50 T_(2,_0,_1) - 0.980198673307 c_1_B + d_(1,_2,_0,_'B')
 >= -50
c06_d_k1_j2_m1_iA: - 50 T_(2,_1,_1) - 0.00990049833749 c_1_A
 + d_(1,_2,_1,_'A') >= -50
c06_d_k1_j2_m1_iB: - 50 T_(2,_1,_1) - 0.0196039734661 c_1_B + d_(1,_2,_1,_'B')
 >= -50
c06_d_k1_j2_m2_iA: - 50 T_(2,_2,_1) - 4.96679133402e-05 c_1_A
 + d_(1,_2,_2,_'A') >= -50
c06_d_k1_j2_m2_iB: - 50 T_(2,_2,_1) - 0.00019735322711 c_1_B
 + d_(1,_2,_2,_'B') >= -50
c06_d_k1_j3_m0_iA: - 50 T_(3,_0,_1) - 0.990049833749 c_1_A + d_(1,_3,_0,_'A')
 >= -50
c06_d_k1_j3_m0_iB: - 50 T_(3,_0,_1) - 0.980198673307 c_1_B + d_(1,_3,_0,_'B')
 >= -50
c06_d_k1_j3_m1_iA: - 50 T_(3,_1,_1) - 0.00990049833749 c_1_A
 + d_(1,_3,_1,_'A') >= -50
c06_d_k1_j3_m1_iB: - 50 T_(3,_1,_1) - 0.0196039734661 c_1_B + d_(1,_3,_1,_'B')
 >= -50
c06_d_k1_j3_m2_iA: - 50 T_(3,_2,_1) - 4.96679133402e-05 c_1_A
 + d_(1,_3,_2,_'A') >= -50
c06_d_k1_j3_m2_iB: - 50 T_(3,_2,_1) - 0.00019735322711 c_1_B
 + d_(1,_3,_2,_'B') >= -50
c06_d_k1_j_1_m0_iA: - 50 T_(_1,_0,_1) - 0.990049833749 c_1_A
 + d_(1,__1,_0,_'A') >= -50
c06_d_k1_j_1_m0_iB: - 50 T_(_1,_0,_1) - 0.980198673307 c_1_B
 + d_(1,__1,_0,_'B') >= -50
c06_d_k1_j_1_m1_iA: - 50 T_(_1,_1,_1) - 0.00990049833749 c_1_A
 + d_(1,__1,_1,_'A') >= -50
c06_d_k1_j_1_m1_iB: - 50 T_(_1,_1,_1) - 0.0196039734661 c_1_B
 + d_(1,__1,_1,_'B') >= -50
c06_d_k1_j_1_m2_iA: - 50 T_(_1,_2,_1) - 4.96679133402e-05 c_1_A
 + d_(1,__1,_2,_'A') >= -50
c06_d_k1_j_1_m2_iB: - 50 T_(_1,_2,_1) - 0.00019735322711 c_1_B
 + d_(1,__1,_2,_'B') >= -50
c06_d_k2_j0_m0_iA: - 50 T_(0,_0,_2) - 0.990049833749 c_2_A + d_(2,_0,_0,_'A')
 >= -50
c06_d_k2_j0_m0_iB: - 50 T_(0,_0,_2) - 0.980198673307 c_2_B + d_(2,_0,_0,_'B')
 >= -50
c06_d_k2_j0_m1_iA: - 50 T_(0,_1,_2) - 0.00990049833749 c_2_A
 + d_(2,_0,_1,_'A') >= -50
c06_d_k2_j0_m1_iB: - 50 T_(0,_1,_2) - 0.0196039734661 c_2_B + d_(2,_0,_1,_'B')
 >= -50
c06_d_k2_j0_m2_iA: - 50 T_(0,_2,_2) - 4.96679133402e-05 c_2_A
 + d_(2,_0,_2,_'A') >= -50
c06_d_k2_j0_m2_iB: - 50 T_(0,_2,_2) - 0.00019735322711 c_2_B
 + d_(2,_0,_2,_'B') >= -50
c06_d_k2_j1_m0_iA: - 50 T_(1,_0,_2) - 0.990049833749 c_2_A + d_(2,_1,_0,_'A')
 >= -50
c06_d_k2_j1_m0_iB: - 50 T_(1,_0,_2) - 0.980198673307 c_2_B + d_(2,_1,_0,_'B')
 >= -50
c06_d_k2_j1_m1_iA: - 50 T_(1,_1,_2) - 0.00990049833749 c_2_A
 + d_(2,_1,_1,_'A') >= -50
c06_d_k2_j1_m1_iB: - 50 T_(1,_1,_2) - 0.0196039734661 c_2_B + d_(2,_1,_1,_'B')
 >= -50
c06_d_k2_j1_m2_iA: - 50 T_(1,_2,_2) - 4.96679133402e-05 c_2_A
 + d_(2,_1,_2,_'A') >= -50
c06_d_k2_j1_m2_iB: - 50 T_(1,_2,_2) - 0.00019735322711 c_2_B
 + d_(2,_1,_2,_'B') >= -50
c06_d_k2_j2_m0_iA: - 50 T_(2,_0,_2) - 0.990049833749 c_2_A + d_(2,_2,_0,_'A')
 >= -50
c06_d_k2_j2_m0_iB: - 50 T_(2,_0,_2) - 0.980198673307 c_2_B + d_(2,_2,_0,_'B')
 >= -50
c06_d_k2_j2_m1_iA: - 50 T_(2,_1,_2) - 0.00990049833749 c_2_A
 + d_(2,_2,_1,_'A') >= -50
c06_d_k2_j2_m1_iB: - 50 T_(2,_1,_2) - 0.0196039734661 c_2_B + d_(2,_2,_1,_'B')
 >= -50
c06_d_k2_j2_m2_iA: - 50 T_(2,_2,_2) - 4.96679133402e-05 c_2_A
 + d_(2,_2,_2,_'A') >= -50
c06_d_k2_j2_m2_iB: - 50 T_(2,_2,_2) - 0.00019735322711 c_2_B
 + d_(2,_2,_2,_'B') >= -50
c06_d_k2_j_1_m0_iA: - 50 T_(_1,_0,_2) - 0.990049833749 c_2_A
 + d_(2,__1,_0,_'A') >= -50
c06_d_k2_j_1_m0_iB: - 50 T_(_1,_0,_2) - 0.980198673307 c_2_B
 + d_(2,__1,_0,_'B') >= -50
c06_d_k2_j_1_m1_iA: - 50 T_(_1,_1,_2) - 0.00990049833749 c_2_A
 + d_(2,__1,_1,_'A') >= -50
c06_d_k2_j_1_m1_iB: - 50 T_(_1,_1,_2) - 0.0196039734661 c_2_B
 + d_(2,__1,_1,_'B') >= -50
c06_d_k2_j_1_m2_iA: - 50 T_(_1,_2,_2) - 4.96679133402e-05 c_2_A
 + d_(2,__1,_2,_'A') >= -50
c06_d_k2_j_1_m2_iB: - 50 T_(_1,_2,_2) - 0.00019735322711 c_2_B
 + d_(2,__1,_2,_'B') >= -50
c06_d_k2_j_2_m0_iA: - 50 T_(_2,_0,_2) - 0.990049833749 c_2_A
 + d_(2,__2,_0,_'A') >= -50
c06_d_k2_j_2_m0_iB: - 50 T_(_2,_0,_2) - 0.980198673307 c_2_B
 + d_(2,__2,_0,_'B') >= -50
c06_d_k2_j_2_m1_iA: - 50 T_(_2,_1,_2) - 0.00990049833749 c_2_A
 + d_(2,__2,_1,_'A') >= -50
c06_d_k2_j_2_m1_iB: - 50 T_(_2,_1,_2) - 0.0196039734661 c_2_B
 + d_(2,__2,_1,_'B') >= -50
c06_d_k2_j_2_m2_iA: - 50 T_(_2,_2,_2) - 4.96679133402e-05 c_2_A
 + d_(2,__2,_2,_'A') >= -50
c06_d_k2_j_2_m2_iB: - 50 T_(_2,_2,_2) - 0.00019735322711 c_2_B
 + d_(2,__2,_2,_'B') >= -50
c06_d_k3_j0_m0_iA: - 50 T_(0,_0,_3) - 0.990049833749 c_3_A + d_(3,_0,_0,_'A')
 >= -50
c06_d_k3_j0_m0_iB: - 50 T_(0,_0,_3) - 0.980198673307 c_3_B + d_(3,_0,_0,_'B')
 >= -50
c06_d_k3_j0_m1_iA: - 50 T_(0,_1,_3) - 0.00990049833749 c_3_A
 + d_(3,_0,_1,_'A') >= -50
c06_d_k3_j0_m1_iB: - 50 T_(0,_1,_3) - 0.0196039734661 c_3_B + d_(3,_0,_1,_'B')
 >= -50
c06_d_k3_j0_m2_iA: - 50 T_(0,_2,_3) - 4.96679133402e-05 c_3_A
 + d_(3,_0,_2,_'A') >= -50
c06_d_k3_j0_m2_iB: - 50 T_(0,_2,_3) - 0.00019735322711 c_3_B
 + d_(3,_0,_2,_'B') >= -50
c06_d_k3_j1_m0_iA: - 50 T_(1,_0,_3) - 0.990049833749 c_3_A + d_(3,_1,_0,_'A')
 >= -50
c06_d_k3_j1_m0_iB: - 50 T_(1,_0,_3) - 0.980198673307 c_3_B + d_(3,_1,_0,_'B')
 >= -50
c06_d_k3_j1_m1_iA: - 50 T_(1,_1,_3) - 0.00990049833749 c_3_A
 + d_(3,_1,_1,_'A') >= -50
c06_d_k3_j1_m1_iB: - 50 T_(1,_1,_3) - 0.0196039734661 c_3_B + d_(3,_1,_1,_'B')
 >= -50
c06_d_k3_j1_m2_iA: - 50 T_(1,_2,_3) - 4.96679133402e-05 c_3_A
 + d_(3,_1,_2,_'A') >= -50
c06_d_k3_j1_m2_iB: - 50 T_(1,_2,_3) - 0.00019735322711 c_3_B
 + d_(3,_1,_2,_'B') >= -50
c06_d_k3_j_1_m0_iA: - 50 T_(_1,_0,_3) - 0.990049833749 c_3_A
 + d_(3,__1,_0,_'A') >= -50
c06_d_k3_j_1_m0_iB: - 50 T_(_1,_0,_3) - 0.980198673307 c_3_B
 + d_(3,__1,_0,_'B') >= -50
c06_d_k3_j_1_m1_iA: - 50 T_(_1,_1,_3) - 0.00990049833749 c_3_A
 + d_(3,__1,_1,_'A') >= -50
c06_d_k3_j_1_m1_iB: - 50 T_(_1,_1,_3) - 0.0196039734661 c_3_B
 + d_(3,__1,_1,_'B') >= -50
c06_d_k3_j_1_m2_iA: - 50 T_(_1,_2,_3) - 4.96679133402e-05 c_3_A
 + d_(3,__1,_2,_'A') >= -50
c06_d_k3_j_1_m2_iB: - 50 T_(_1,_2,_3) - 0.00019735322711 c_3_B
 + d_(3,__1,_2,_'B') >= -50
c06_d_k3_j_2_m0_iA: - 50 T_(_2,_0,_3) - 0.990049833749 c_3_A
 + d_(3,__2,_0,_'A') >= -50
c06_d_k3_j_2_m0_iB: - 50 T_(_2,_0,_3) - 0.980198673307 c_3_B
 + d_(3,__2,_0,_'B') >= -50
c06_d_k3_j_2_m1_iA: - 50 T_(_2,_1,_3) - 0.00990049833749 c_3_A
 + d_(3,__2,_1,_'A') >= -50
c06_d_k3_j_2_m1_iB: - 50 T_(_2,_1,_3) - 0.0196039734661 c_3_B
 + d_(3,__2,_1,_'B') >= -50
c06_d_k3_j_2_m2_iA: - 50 T_(_2,_2,_3) - 4.96679133402e-05 c_3_A
 + d_(3,__2,_2,_'A') >= -50
c06_d_k3_j_2_m2_iB: - 50 T_(_2,_2,_3) - 0.00019735322711 c_3_B
 + d_(3,__2,_2,_'B') >= -50
c06_d_k3_j_3_m0_iA: - 50 T_(_3,_0,_3) - 0.990049833749 c_3_A
 + d_(3,__3,_0,_'A') >= -50
c06_d_k3_j_3_m0_iB: - 50 T_(_3,_0,_3) - 0.980198673307 c_3_B
 + d_(3,__3,_0,_'B') >= -50
c06_d_k3_j_3_m1_iA: - 50 T_(_3,_1,_3) - 0.00990049833749 c_3_A
 + d_(3,__3,_1,_'A') >= -50
c06_d_k3_j_3_m1_iB: - 50 T_(_3,_1,_3) - 0.0196039734661 c_3_B
 + d_(3,__3,_1,_'B') >= -50
c06_d_k3_j_3_m2_iA: - 50 T_(_3,_2,_3) - 4.96679133402e-05 c_3_A
 + d_(3,__3,_2,_'A') >= -50
c06_d_k3_j_3_m2_iB: - 50 T_(_3,_2,_3) - 0.00019735322711 c_3_B
 + d_(3,__3,_2,_'B') >= -50
c06_d_k4_j0_m0_iA: - 50 T_(0,_0,_4) - 0.990049833749 c_4_A + d_(4,_0,_0,_'A')
 >= -50
c06_d_k4_j0_m0_iB: - 50 T_(0,_0,_4) - 0.980198673307 c_4_B + d_(4,_0,_0,_'B')
 >= -50
c06_d_k4_j0_m1_iA: - 50 T_(0,_1,_4) - 0.00990049833749 c_4_A
 + d_(4,_0,_1,_'A') >= -50
c06_d_k4_j0_m1_iB: - 50 T_(0,_1,_4) - 0.0196039734661 c_4_B + d_(4,_0,_1,_'B')
 >= -50
c06_d_k4_j0_m2_iA: - 50 T_(0,_2,_4) - 4.96679133402e-05 c_4_A
 + d_(4,_0,_2,_'A') >= -50
c06_d_k4_j0_m2_iB: - 50 T_(0,_2,_4) - 0.00019735322711 c_4_B
 + d_(4,_0,_2,_'B') >= -50
c06_d_k4_j_1_m0_iA: - 50 T_(_1,_0,_4) - 0.990049833749 c_4_A
 + d_(4,__1,_0,_'A') >= -50
c06_d_k4_j_1_m0_iB: - 50 T_(_1,_0,_4) - 0.980198673307 c_4_B
 + d_(4,__1,_0,_'B') >= -50
c06_d_k4_j_1_m1_iA: - 50 T_(_1,_1,_4) - 0.00990049833749 c_4_A
 + d_(4,__1,_1,_'A') >= -50
c06_d_k4_j_1_m1_iB: - 50 T_(_1,_1,_4) - 0.0196039734661 c_4_B
 + d_(4,__1,_1,_'B') >= -50
c06_d_k4_j_1_m2_iA: - 50 T_(_1,_2,_4) - 4.96679133402e-05 c_4_A
 + d_(4,__1,_2,_'A') >= -50
c06_d_k4_j_1_m2_iB: - 50 T_(_1,_2,_4) - 0.00019735322711 c_4_B
 + d_(4,__1,_2,_'B') >= -50
c06_d_k4_j_2_m0_iA: - 50 T_(_2,_0,_4) - 0.990049833749 c_4_A
 + d_(4,__2,_0,_'A') >= -50
c06_d_k4_j_2_m0_iB: - 50 T_(_2,_0,_4) - 0.980198673307 c_4_B
 + d_(4,__2,_0,_'B') >= -50
c06_d_k4_j_2_m1_iA: - 50 T_(_2,_1,_4) - 0.00990049833749 c_4_A
 + d_(4,__2,_1,_'A') >= -50
c06_d_k4_j_2_m1_iB: - 50 T_(_2,_1,_4) - 0.0196039734661 c_4_B
 + d_(4,__2,_1,_'B') >= -50
c06_d_k4_j_2_m2_iA: - 50 T_(_2,_2,_4) - 4.96679133402e-05 c_4_A
 + d_(4,__2,_2,_'A') >= -50
c06_d_k4_j_2_m2_iB: - 50 T_(_2,_2,_4) - 0.00019735322711 c_4_B
 + d_(4,__2,_2,_'B') >= -50
c06_d_k4_j_3_m0_iA: - 50 T_(_3,_0,_4) - 0.990049833749 c_4_A
 + d_(4,__3,_0,_'A') >= -50
c06_d_k4_j_3_m0_iB: - 50 T_(_3,_0,_4) - 0.980198673307 c_4_B
 + d_(4,__3,_0,_'B') >= -50
c06_d_k4_j_3_m1_iA: - 50 T_(_3,_1,_4) - 0.00990049833749 c_4_A
 + d_(4,__3,_1,_'A') >= -50
c06_d_k4_j_3_m1_iB: - 50 T_(_3,_1,_4) - 0.0196039734661 c_4_B
 + d_(4,__3,_1,_'B') >= -50
c06_d_k4_j_3_m2_iA: - 50 T_(_3,_2,_4) - 4.96679133402e-05 c_4_A
 + d_(4,__3,_2,_'A') >= -50
c06_d_k4_j_3_m2_iB: - 50 T_(_3,_2,_4) - 0.00019735322711 c_4_B
 + d_(4,__3,_2,_'B') >= -50
c06_d_k4_j_4_m0_iA: - 50 T_(_4,_0,_4) - 0.990049833749 c_4_A
 + d_(4,__4,_0,_'A') >= -50
c06_d_k4_j_4_m0_iB: - 50 T_(_4,_0,_4) - 0.980198673307 c_4_B
 + d_(4,__4,_0,_'B') >= -50
c06_d_k4_j_4_m1_iA: - 50 T_(_4,_1,_4) - 0.00990049833749 c_4_A
 + d_(4,__4,_1,_'A') >= -50
c06_d_k4_j_4_m1_iB: - 50 T_(_4,_1,_4) - 0.0196039734661 c_4_B
 + d_(4,__4,_1,_'B') >= -50
c06_d_k4_j_4_m2_iA: - 50 T_(_4,_2,_4) - 4.96679133402e-05 c_4_A
 + d_(4,__4,_2,_'A') >= -50
c06_d_k4_j_4_m2_iB: - 50 T_(_4,_2,_4) - 0.00019735322711 c_4_B
 + d_(4,__4,_2,_'B') >= -50
c09_trk_k0_iA: c_0_A - d_(0,_0,_0,_'A') - d_(0,_0,_1,_'A') - d_(0,_0,_2,_'A')
 - d_(1,__1,_0,_'A') - d_(1,__1,_1,_'A') - d_(1,__1,_2,_'A')
 - d_(2,__2,_0,_'A') - d_(2,__2,_1,_'A') - d_(2,__2,_2,_'A')
 - d_(3,__3,_0,_'A') - d_(3,__3,_1,_'A') - d_(3,__3,_2,_'A')
 - d_(4,__4,_0,_'A') - d_(4,__4,_1,_'A') - d_(4,__4,_2,_'A') = 0
c09_trk_k0_iB: c_0_B - d_(0,_0,_0,_'B') - d_(0,_0,_1,_'B') - d_(0,_0,_2,_'B')
 - d_(1,__1,_0,_'B') - d_(1,__1,_1,_'B') - d_(1,__1,_2,_'B')
 - d_(2,__2,_0,_'B') - d_(2,__2,_1,_'B') - d_(2,__2,_2,_'B')
 - d_(3,__3,_0,_'B') - d_(3,__3,_1,_'B') - d_(3,__3,_2,_'B')
 - d_(4,__4,_0,_'B') - d_(4,__4,_1,_'B') - d_(4,__4,_2,_'B') = 0
c09_trk_k1_iA: c_1_A - d_(0,_1,_0,_'A') - d_(0,_1,_1,_'A') - d_(0,_1,_2,_'A')
 - d_(1,_0,_0,_'A') - d_(1,_0,_1,_'A') - d_(1,_0,_2,_'A') - d_(2,__1,_0,_'A')
 - d_(2,__1,_1,_'A') - d_(2,__1,_2,_'A') - d_(3,__2,_0,_'A')
 - d_(3,__2,_1,_'A') - d_(3,__2,_2,_'A') - d_(4,__3,_0,_'A')
 - d_(4,__3,_1,_'A') - d_(4,__3,_2,_'A') = 0
c09_trk_k1_iB: c_1_B - d_(0,_1,_0,_'B') - d_(0,_1,_1,_'B') - d_(0,_1,_2,_'B')
 - d_(1,_0,_0,_'B') - d_(1,_0,_1,_'B') - d_(1,_0,_2,_'B') - d_(2,__1,_0,_'B')
 - d_(2,__1,_1,_'B') - d_(2,__1,_2,_'B') - d_(3,__2,_0,_'B')
 - d_(3,__2,_1,_'B') - d_(3,__2,_2,_'B') - d_(4,__3,_0,_'B')
 - d_(4,__3,_1,_'B') - d_(4,__3,_2,_'B') = 0
c09_trk_k2_iA: c_2_A - d_(0,_2,_0,_'A') - d_(0,_2,_1,_'A') - d_(0,_2,_2,_'A')
 - d_(1,_1,_0,_'A') - d_(1,_1,_1,_'A') - d_(1,_1,_2,_'A') - d_(2,_0,_0,_'A')
 - d_(2,_0,_1,_'A') - d_(2,_0,_2,_'A') - d_(3,__1,_0,_'A') - d_(3,__1,_1,_'A')
 - d_(3,__1,_2,_'A') - d_(4,__2,_0,_'A') - d_(4,__2,_1,_'A')
 - d_(4,__2,_2,_'A') = 0
c09_trk_k2_iB: c_2_B - d_(0,_2,_0,_'B') - d_(0,_2,_1,_'B') - d_(0,_2,_2,_'B')
 - d_(1,_1,_0,_'B') - d_(1,_1,_1,_'B') - d_(1,_1,_2,_'B') - d_(2,_0,_0,_'B')
 - d_(2,_0,_1,_'B') - d_(2,_0,_2,_'B') - d_(3,__1,_0,_'B') - d_(3,__1,_1,_'B')
 - d_(3,__1,_2,_'B') - d_(4,__2,_0,_'B') - d_(4,__2,_1,_'B')
 - d_(4,__2,_2,_'B') = 0
c09_trk_k3_iA: c_3_A - d_(0,_3,_0,_'A') - d_(0,_3,_1,_'A') - d_(0,_3,_2,_'A')
 - d_(1,_2,_0,_'A') - d_(1,_2,_1,_'A') - d_(1,_2,_2,_'A') - d_(2,_1,_0,_'A')
 - d_(2,_1,_1,_'A') - d_(2,_1,_2,_'A') - d_(3,_0,_0,_'A') - d_(3,_0,_1,_'A')
 - d_(3,_0,_2,_'A') - d_(4,__1,_0,_'A') - d_(4,__1,_1,_'A')
 - d_(4,__1,_2,_'A') = 0
c09_trk_k3_iB: c_3_B - d_(0,_3,_0,_'B') - d_(0,_3,_1,_'B') - d_(0,_3,_2,_'B')
 - d_(1,_2,_0,_'B') - d_(1,_2,_1,_'B') - d_(1,_2,_2,_'B') - d_(2,_1,_0,_'B')
 - d_(2,_1,_1,_'B') - d_(2,_1,_2,_'B') - d_(3,_0,_0,_'B') - d_(3,_0,_1,_'B')
 - d_(3,_0,_2,_'B') - d_(4,__1,_0,_'B') - d_(4,__1,_1,_'B')
 - d_(4,__1,_2,_'B') = 0
c09_trk_k4_iA: c_4_A - d_(0,_4,_0,_'A') - d_(0,_4,_1,_'A') - d_(0,_4,_2,_'A')
 - d_(1,_3,_0,_'A') - d_(1,_3,_1,_'A') - d_(1,_3,_2,_'A') - d_(2,_2,_0,_'A')
 - d_(2,_2,_1,_'A') - d_(2,_2,_2,_'A') - d_(3,_1,_0,_'A') - d_(3,_1,_1,_'A')
 - d_(3,_1,_2,_'A') - d_(4,_0,_0,_'A') - d_(4,_0,_1,_'A') - d_(4,_0,_2,_'A')
 = 0
c09_trk_k4_iB: c_4_B - d_(0,_4,_0,_'B') - d_(0,_4,_1,_'B') - d_(0,_4,_2,_'B')
 - d_(1,_3,_0,_'B') - d_(1,_3,_1,_'B') - d_(1,_3,_2,_'B') - d_(2,_2,_0,_'B')
 - d_(2,_2,_1,_'B') - d_(2,_2,_2,_'B') - d_(3,_1,_0,_'B') - d_(3,_1,_1,_'B')
 - d_(3,_1,_2,_'B') - d_(4,_0,_0,_'B') - d_(4,_0,_1,_'B') - d_(4,_0,_2,_'B')
 = 0
c14_g_elteres_p_k0_iA: 0 c_0_A + g_0_A + o_0_0_A >= 0
c14_g_elteres_p_k0_iB: - 0.01 c_0_B + g_0_B + o_0_0_B >= 0
c14_g_elteres_p_k1_iA: 0 c_1_A + g_1_A + o_1_0_A >= 0
c14_g_elteres_p_k1_iB: - 0.01 c_1_B + g_1_B + o_1_0_B >= 0
c14_g_elteres_p_k2_iA: 0 c_2_A + g_2_A + o_2_0_A >= 0
c14_g_elteres_p_k2_iB: - 0.01 c_2_B + g_2_B + o_2_0_B >= 0
c14_g_elteres_p_k3_iA: 0 c_3_A + g_3_A + o_3_0_A >= 0
c14_g_elteres_p_k3_iB: - 0.01 c_3_B + g_3_B + o_3_0_B >= 0
c14_g_elteres_p_k4_iA: 0 c_4_A + g_4_A + o_4_0_A >= 0
c14_g_elteres_p_k4_iB: - 0.01 c_4_B + g_4_B + o_4_0_B >= 0
c14b_g_elteres_n_k0_iA: 0 c_0_A - g_0_A + o_0_0_A <= 0
c14b_g_elteres_n_k0_iB: - 0.01 c_0_B - g_0_B + o_0_0_B <= 0
c14b_g_elteres_n_k1_iA: 0 c_1_A - g_1_A + o_1_0_A <= 0
c14b_g_elteres_n_k1_iB: - 0.01 c_1_B - g_1_B + o_1_0_B <= 0
c14b_g_elteres_n_k2_iA: 0 c_2_A - g_2_A + o_2_0_A <= 0
c14b_g_elteres_n_k2_iB: - 0.01 c_2_B - g_2_B + o_2_0_B <= 0
c14b_g_elteres_n_k3_iA: 0 c_3_A - g_3_A + o_3_0_A <= 0
c14b_g_elteres_n_k3_iB: - 0.01 c_3_B - g_3_B + o_3_0_B <= 0
c14b_g_elteres_n_k4_iA: 0 c_4_A - g_4_A + o_4_0_A <= 0
c14b_g_elteres_n_k4_iB: - 0.01 c_4_B - g_4_B + o_4_0_B <= 0
c16_dijmon_k0: 0.01 O_0_0 - 0.01 O_1_0 >= 0
c16_dijmon_k1: 0.01 O_1_0 - 0.01 O_2_0 >= 0
c16_dijmon_k2: 0.01 O_2_0 - 0.01 O_3_0 >= 0
c16_dijmon_k3: 0.01 O_3_0 - 0.01 O_4_0 >= 0
c17a_op_also_k0_l0_iA: - 0.5 O_0_0 - 0.01 c_0_A + o_0_0_A >= -0.5
c17a_op_also_k0_l0_iB: - 0.5 O_0_0 - 0.01 c_0_B + o_0_0_B >= -0.5
c17a_op_also_k1_l0_iA: - 0.5 O_1_0 - 0.01 c_1_A + o_1_0_A >= -0.5
c17a_op_also_k1_l0_iB: - 0.5 O_1_0 - 0.01 c_1_B + o_1_0_B >= -0.5
c17a_op_also_k2_l0_iA: - 0.5 O_2_0 - 0.01 c_2_A + o_2_0_A >= -0.5
c17a_op_also_k2_l0_iB: - 0.5 O_2_0 - 0.01 c_2_B + o_2_0_B >= -0.5
c17a_op_also_k3_l0_iA: - 0.5 O_3_0 - 0.01 c_3_A + o_3_0_A >= -0.5
c17a_op_also_k3_l0_iB: - 0.5 O_3_0 - 0.01 c_3_B + o_3_0_B >= -0.5
c17a_op_also_k4_l0_iA: - 0.5 O_4_0 - 0.01 c_4_A + o_4_0_A >= -0.5
c17a_op_also_k4_l0_iB: - 0.5 O_4_0 - 0.01 c_4_B + o_4_0_B >= -0.5
c17b_op_felso_k0_l0_iA: - 0.01 c_0_A + o_0_0_A <= 0
c17b_op_felso_k0_l0_iB: - 0.01 c_0_B + o_0_0_B <= 0
c17b_op_felso_k1_l0_iA: - 0.01 c_1_A + o_1_0_A <= 0
c17b_op_felso_k1_l0_iB: - 0.01 c_1_B + o_1_0_B <= 0
c17b_op_felso_k2_l0_iA: - 0.01 c_2_A + o_2_0_A <= 0
c17b_op_felso_k2_l0_iB: - 0.01 c_2_B + o_2_0_B <= 0
c17b_op_felso_k3_l0_iA: - 0.01 c_3_A + o_3_0_A <= 0
c17b_op_felso_k3_l0_iB: - 0.01 c_3_B + o_3_0_B <= 0
c17b_op_felso_k4_l0_iA: - 0.01 c_4_A + o_4_0_A <= 0
c17b_op_felso_k4_l0_iB: - 0.01 c_4_B + o_4_0_B <= 0
c17c_op_bin_k0_l0_iA: - 0.5 O_0_0 + o_0_0_A <= 0
c17c_op_bin_k0_l0_iB: - 0.5 O_0_0 + o_0_0_B <= 0
c17c_op_bin_k1_l0_iA: - 0.5 O_1_0 + o_1_0_A <= 0
c17c_op_bin_k1_l0_iB: - 0.5 O_1_0 + o_1_0_B <= 0
c17c_op_bin_k2_l0_iA: - 0.5 O_2_0 + o_2_0_A <= 0
c17c_op_bin_k2_l0_iB: - 0.5 O_2_0 + o_2_0_B <= 0
c17c_op_bin_k3_l0_iA: - 0.5 O_3_0 + o_3_0_A <= 0
c17c_op_bin_k3_l0_iB: - 0.5 O_3_0 + o_3_0_B <= 0
c17c_op_bin_k4_l0_iA: - 0.5 O_4_0 + o_4_0_A <= 0
c17c_op_bin_k4_l0_iB: - 0.5 O_4_0 + o_4_0_B <= 0
c18_egyvalt0: O_0_0 <= 1
c18_egyvalt1: O_1_0 <= 1
c18_egyvalt2: O_2_0 <= 1
c18_egyvalt3: O_3_0 <= 1
c18_egyvalt4: O_4_0 <= 1
Bounds
0 <= c_0_A
0 <= c_0_B
0 <= c_1_A
0 <= c_1_B
0 <= c_2_A
0 <= c_2_B
0 <= c_3_A
0 <= c_3_B
0 <= c_4_A
0 <= c_4_B
0 <= d_(0,_0,_0,_'A')
0 <= d_(0,_0,_0,_'B')
0 <= d_(0,_0,_1,_'A')
0 <= d_(0,_0,_1,_'B')
0 <= d_(0,_0,_2,_'A')
0 <= d_(0,_0,_2,_'B')
0 <= d_(0,_1,_0,_'A')
0 <= d_(0,_1,_0,_'B')
0 <= d_(0,_1,_1,_'A')
0 <= d_(0,_1,_1,_'B')
0 <= d_(0,_1,_2,_'A')
0 <= d_(0,_1,_2,_'B')
0 <= d_(0,_2,_0,_'A')
0 <= d_(0,_2,_0,_'B')
0 <= d_(0,_2,_1,_'A')
0 <= d_(0,_2,_1,_'B')
0 <= d_(0,_2,_2,_'A')
0 <= d_(0,_2,_2,_'B')
0 <= d_(0,_3,_0,_'A')
0 <= d_(0,_3,_0,_'B')
0 <= d_(0,_3,_1,_'A')
0 <= d_(0,_3,_1,_'B')
0 <= d_(0,_3,_2,_'A')
0 <= d_(0,_3,_2,_'B')
0 <= d_(0,_4,_0,_'A')
0 <= d_(0,_4,_0,_'B')
0 <= d_(0,_4,_1,_'A')
0 <= d_(0,_4,_1,_'B')
0 <= d_(0,_4,_2,_'A')
0 <= d_(0,_4,_2,_'B')
0 <= d_(1,_0,_0,_'A')
0 <= d_(1,_0,_0,_'B')
0 <= d_(1,_0,_1,_'A')
0 <= d_(1,_0,_1,_'B')
0 <= d_(1,_0,_2,_'A')
0 <= d_(1,_0,_2,_'B')
0 <= d_(1,_1,_0,_'A')
0 <= d_(1,_1,_0,_'B')
0 <= d_(1,_1,_1,_'A')
0 <= d_(1,_1,_1,_'B')
0 <= d_(1,_1,_2,_'A')
0 <= d_(1,_1,_2,_'B')
0 <= d_(1,_2,_0,_'A')
0 <= d_(1,_2,_0,_'B')
0 <= d_(1,_2,_1,_'A')
0 <= d_(1,_2,_1,_'B')
0 <= d_(1,_2,_2,_'A')
0 <= d_(1,_2,_2,_'B')
0 <= d_(1,_3,_0,_'A')
0 <= d_(1,_3,_0,_'B')
0 <= d_(1,_3,_1,_'A')
0 <= d_(1,_3,_1,_'B')
0 <= d_(1,_3,_2,_'A')
0 <= d_(1,_3,_2,_'B')
0 <= d_(1,__1,_0,_'A')
0 <= d_(1,__1,_0,_'B')
0 <= d_(1,__1,_1,_'A')
0 <= d_(1,__1,_1,_'B')
0 <= d_(1,__1,_2,_'A')
0 <= d_(1,__1,_2,_'B')
0 <= d_(2,_0,_0,_'A')
0 <= d_(2,_0,_0,_'B')
0 <= d_(2,_0,_1,_'A')
0 <= d_(2,_0,_1,_'B')
0 <= d_(2,_0,_2,_'A')
0 <= d_(2,_0,_2,_'B')
0 <= d_(2,_1,_0,_'A')
0 <= d_(2,_1,_0,_'B')
0 <= d_(2,_1,_1,_'A')
0 <= d_(2,_1,_1,_'B')
0 <= d_(2,_1,_2,_'A')
0 <= d_(2,_1,_2,_'B')
0 <= d_(2,_2,_0,_'A')
0 <= d_(2,_2,_0,_'B')
0 <= d_(2,_2,_1,_'A')
0 <= d_(2,_2,_1,_'B')
0 <= d_(2,_2,_2,_'A')
0 <= d_(2,_2,_2,_'B')
0 <= d_(2,__1,_0,_'A')
0 <= d_(2,__1,_0,_'B')
0 <= d_(2,__1,_1,_'A')
0 <= d_(2,__1,_1,_'B')
0 <= d_(2,__1,_2,_'A')
0 <= d_(2,__1,_2,_'B')
0 <= d_(2,__2,_0,_'A')
0 <= d_(2,__2,_0,_'B')
0 <= d_(2,__2,_1,_'A')
0 <= d_(2,__2,_1,_'B')
0 <= d_(2,__2,_2,_'A')
0 <= d_(2,__2,_2,_'B')
0 <= d_(3,_0,_0,_'A')
0 <= d_(3,_0,_0,_'B')
0 <= d_(3,_0,_1,_'A')
0 <= d_(3,_0,_1,_'B')
0 <= d_(3,_0,_2,_'A')
0 <= d_(3,_0,_2,_'B')
0 <= d_(3,_1,_0,_'A')
0 <= d_(3,_1,_0,_'B')
0 <= d_(3,_1,_1,_'A')
0 <= d_(3,_1,_1,_'B')
0 <= d_(3,_1,_2,_'A')
0 <= d_(3,_1,_2,_'B')
0 <= d_(3,__1,_0,_'A')
0 <= d_(3,__1,_0,_'B')
0 <= d_(3,__1,_1,_'A')
0 <= d_(3,__1,_1,_'B')
0 <= d_(3,__1,_2,_'A')
0 <= d_(3,__1,_2,_'B')
0 <= d_(3,__2,_0,_'A')
0 <= d_(3,__2,_0,_'B')
0 <= d_(3,__2,_1,_'A')
0 <= d_(3,__2,_1,_'B')
0 <= d_(3,__2,_2,_'A')
0 <= d_(3,__2,_2,_'B')
0 <= d_(3,__3,_0,_'A')
0 <= d_(3,__3,_0,_'B')
0 <= d_(3,__3,_1,_'A')
0 <= d_(3,__3,_1,_'B')
0 <= d_(3,__3,_2,_'A')
0 <= d_(3,__3,_2,_'B')
0 <= d_(4,_0,_0,_'A')
0 <= d_(4,_0,_0,_'B')
0 <= d_(4,_0,_1,_'A')
0 <= d_(4,_0,_1,_'B')
0 <= d_(4,_0,_2,_'A')
0 <= d_(4,_0,_2,_'B')
0 <= d_(4,__1,_0,_'A')
0 <= d_(4,__1,_0,_'B')
0 <= d_(4,__1,_1,_'A')
0 <= d_(4,__1,_1,_'B')
0 <= d_(4,__1,_2,_'A')
0 <= d_(4,__1,_2,_'B')
0 <= d_(4,__2,_0,_'A')
0 <= d_(4,__2,_0,_'B')
0 <= d_(4,__2,_1,_'A')
0 <= d_(4,__2,_1,_'B')
0 <= d_(4,__2,_2,_'A')
0 <= d_(4,__2,_2,_'B')
0 <= d_(4,__3,_0,_'A')
0 <= d_(4,__3,_0,_'B')
0 <= d_(4,__3,_1,_'A')
0 <= d_(4,__3,_1,_'B')
0 <= d_(4,__3,_2,_'A')
0 <= d_(4,__3,_2,_'B')
0 <= d_(4,__4,_0,_'A')
0 <= d_(4,__4,_0,_'B')
0 <= d_(4,__4,_1,_'A')
0 <= d_(4,__4,_1,_'B')
0 <= d_(4,__4,_2,_'A')
0 <= d_(4,__4,_2,_'B')
0 <= g_0_A
0 <= g_0_B
0 <= g_1_A
0 <= g_1_B
0 <= g_2_A
0 <= g_2_B
0 <= g_3_A
0 <= g_3_B
0 <= g_4_A
0 <= g_4_B
0 <= o_0_0_A
0 <= o_0_0_B
0 <= o_1_0_A
0 <= o_1_0_B
0 <= o_2_0_A
0 <= o_2_0_B
0 <= o_3_0_A
0 <= o_3_0_B
0 <= o_4_0_A
0 <= o_4_0_B
Binaries
O_0_0
O_1_0
O_2_0
O_3_0
O_4_0
T_(0,_0,_0)
T_(0,_0,_1)
T_(0,_0,_2)
T_(0,_0,_3)
T_(0,_0,_4)
T_(0,_1,_0)
T_(0,_1,_1)
T_(0,_1,_2)
T_(0,_1,_3)
T_(0,_1,_4)
T_(0,_2,_0)
T_(0,_2,_1)
T_(0,_2,_2)
T_(0,_2,_3)
T_(0,_2,_4)
T_(1,_0,_0)
T_(1,_0,_1)
T_(1,_0,_2)
T_(1,_0,_3)
T_(1,_1,_0)
T_(1,_1,_1)
T_(1,_1,_2)
T_(1,_1,_3)
T_(1,_2,_0)
T_(1,_2,_1)
T_(1,_2,_2)
T_(1,_2,_3)
T_(2,_0,_0)
T_(2,_0,_1)
T_(2,_0,_2)
T_(2,_1,_0)
T_(2,_1,_1)
T_(2,_1,_2)
T_(2,_2,_0)
T_(2,_2,_1)
T_(2,_2,_2)
T_(3,_0,_0)
T_(3,_0,_1)
T_(3,_1,_0)
T_(3,_1,_1)
T_(3,_2,_0)
T_(3,_2,_1)
T_(4,_0,_0)
T_(4,_1,_0)
T_(4,_2,_0)
T_(_1,_0,_1)
T_(_1,_0,_2)
T_(_1,_0,_3)
T_(_1,_0,_4)
T_(_1,_1,_1)
T_(_1,_1,_2)
T_(_1,_1,_3)
T_(_1,_1,_4)
T_(_1,_2,_1)
T_(_1,_2,_2)
T_(_1,_2,_3)
T_(_1,_2,_4)
T_(_2,_0,_2)
T_(_2,_0,_3)
T_(_2,_0,_4)
T_(_2,_1,_2)
T_(_2,_1,_3)
T_(_2,_1,_4)
T_(_2,_2,_2)
T_(_2,_2,_3)
T_(_2,_2,_4)
T_(_3,_0,_3)
T_(_3,_0,_4)
T_(_3,_1,_3)
T_(_3,_1,_4)
T_(_3,_2,_3)
T_(_3,_2,_4)
T_(_4,_0,_4)
T_(_4,_1,_4)
T_(_4,_2,_4)
End
