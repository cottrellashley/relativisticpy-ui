

Constants = {
            "Default": "",
            "Schwarzschild" : "[[-(1 - (G)/(r)),0,0,0],[0,1/(1 - (G)/(r)),0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "SchildGeneral" : "[[-F(r),0,0,0],[0,1/(F(r)),0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "AntiDeSitter" : "[[-(k**2*r**2 + 1),0,0,0],[0,1/(k**2*r**2 + 1),0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "PolarCoordinates" : "[[-1,0,0,0],[0,1,0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "Minkowski" : "[[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]",
            "WeylLewisPapapetrou": "[[-1,0,0,0],[0,1,0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "ReissnerNordström" : "[[-(1 - (G)/(r) + (Q**2)/(r**2)),0,0,0],[0,1/(1 - (G)/(r) + (Q**2)/(r**2)),0,0],[0,0,r**2,0],[0,0,0,r**2*sin(theta)**2]]",
            "PolarBasis" : "[t, r, theta, phi]",
            "MinkBasis" : "[t, x, y, z]",
            "OperationsList" : ["Gamma","Derivative","Inverse Metric","Ricci","Covariant Riemann","Riemann","Ricci Scalar","K-Scalar","CovarientD01","CovarientD10","CovarientD11","CovarientD02","CovarientD20"],
            "All_Valid_Words" : ["theta","phi","omega","sigma","alpha","beta","gamma","epsilon","zeta","eta","kappa","lambda","mu","nu","pi",
                                  "Theta","Phi","Omega","Sigma","Alpha","Beta","Gamma","Epsilon","Zeta","Eta","Kappa","Lambda","Mu","Nu","Pi",
                                  "sin","cos","tan","sinh","cosh","tanh","asin","atan","acos","asinh","acosh","atanh","exp","pi","Derivative",
                                 "dsolve", "solve", "integrate", "Subs", "simplify", "T1", "T2", "T3", "T4", "T5"],
            "Valid_Basis_Words" : ["theta","phi","omega","sigma","alpha","beta","gamma","epsilon","zeta","eta","kappa","lambda","mu","nu"]
}