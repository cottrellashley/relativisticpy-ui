# --- Home page ----
with open('./Constants/WelcomePage/SideNote.md', 'r') as _: SideNote = _.read()
with open('./Constants/WelcomePage/SupportedEquations.md', 'r') as _: SupportedEquations = _.read()
with open('./Constants/WelcomePage/WelcomingMessage.md', 'r') as _: WelcomingMessage = _.read()
with open('./Constants/BackgroundKnowledge/GRSummary.md', 'r') as _: OverviewSummary = _.read()
with open('./Constants/BackgroundKnowledge/TheMetric.md', 'r') as _: TheMetric = _.read()
with open('./Constants/BackgroundKnowledge/CovariantDerivative.md', 'r') as _: CovariantDerivative = _.read()
with open('./Constants/BackgroundKnowledge/Gamma.md', 'r') as _: Gamma = _.read()
with open('./Constants/BackgroundKnowledge/RiemannCurvatureTensor.md', 'r') as _: RiemannCurvatureTensor = _.read()
with open('./Constants/BackgroundKnowledge/RicciTensor.md', 'r') as _: RicciTensor = _.read()
with open('./Constants/BackgroundKnowledge/TheEinsteinEquation.md', 'r') as _: TheEinsteinEquation = _.read()
with open('./Constants/AboutMe/AboutMe.md', 'r') as _: AboutMe = _.read()


# --- Calculator Page ----
with open('./Constants/HowToUse/MetricRules.md', 'r') as _: MetricRules = _.read()
with open('./Constants/HowToUse/BasisRules.md', 'r') as _: BasisRules = _.read()
with open('./Constants/HowToUse/AnswerRules.md', 'r') as _: AnswerRules = _.read()
# -Use Case-
with open('./Constants/UseCase/Step1.md', 'r') as _: Step1 = _.read()
with open('./Constants/UseCase/Step2.md', 'r') as _: Step2 = _.read()
with open('./Constants/UseCase/Step3.md', 'r') as _: Step3 = _.read()
with open('./Constants/UseCase/Step4.md', 'r') as _: Step4 = _.read()
with open('./Constants/UseCase/Step5.md', 'r') as _: Step5 = _.read()
with open('./Constants/UseCase/Step6.md', 'r') as _: Step6 = _.read()


with open('./Constants/styleEquationOutput.md', 'r') as _: styleEquationOutput = _.read()

MarkdownFiles = {
            "OverviewSummary" : OverviewSummary,
            "WelcomingMessage" : WelcomingMessage,
            "AboutMe" : AboutMe,
            "TheMetric" : TheMetric,
            "CovariantDerivative"   : CovariantDerivative,
            "Gamma" : Gamma,
            "RiemannCurvatureTensor": RiemannCurvatureTensor,
            "RicciTensor":RicciTensor,
            "TheEinsteinEquation":TheEinsteinEquation,
            "SideNote" : SideNote,
            "MetricRules" : MetricRules,
            "BasisRules": BasisRules,
            "AnswerRules": AnswerRules,
            "EquationOutputStyle" : styleEquationOutput,
            "Step1": Step1,
            "Step2": Step2,
            "Step3": Step3,
            "Step4": Step4,
            "Step5": Step5,
            "Step6": Step6,
            "SupportedEquations" : SupportedEquations
}