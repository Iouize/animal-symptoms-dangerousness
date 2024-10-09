from sklearn.base import BaseEstimator, TransformerMixin

def clean(word):

    for char in ['_', '-', ',', '\xa0', ' ', '.', ')', '(']:
        word = word.replace(char, ' ')

    replace_words = {"head ache" : "headache", "anversion": "aversion", "thivk": "thick", " oh ":" of "}
    for bad_word in replace_words:
        word = word.replace(bad_word, replace_words[bad_word])

    word = word.lower().strip()

    return word

def change(df, ws, new):
    symps = ['symptoms1', 'symptoms2', 'symptoms3', 'symptoms4', 'symptoms5']
    for col in symps:
        for w in ws:
            df[col] = df[col].replace(w, new, regex=True)
    return df


class DataCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, clean_func, change_func):
        self.clean_func = clean_func
        self.change_func = change_func

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        # X = X.dropna(how='any', axis=0)
        # X.drop_duplicates(inplace=True)
        for col in X.columns:
            X[col] = X[col].apply(self.clean_func)

        X = self.change_func(X, ws = ['difficultty in breathing', 'difficulty in breathing', 'difficulty breating', 'difficulty breathing','diffculty breathing', 'difficulty breathing', 'labored breathing', 'lound breathing', 'respiratory noise', 'respiratory distress','gasping for breath', 'gasping for air'], new = 'breathing difficulty')
        X = self.change_func(X, ws = ['difficulty in walking', 'difficult in walking','limp', 'lip', 'inability to stand','difficulty in walk', 'difficulty walking', 'walking problem','lameness', 'legness'], new = 'walking difficulty')
        X = self.change_func(X, ws = ['high body temperaure', 'high body temperature'], new = 'high body temperature')
        X = self.change_func(X, ws = ['discharge from eye', 'discharge from eyes'], new = 'discharge from eyes')
        X = self.change_func(X, ws = ['decreased appetite', 'decrease appetite', 'poor appetite','loss of eat', 'loss of appettite', 'loss of appetite', 'reduced appetite','loss od appetite', 'loss of appetite', 'unable to eat','loss of appetite', 'lack of appetite'], new = 'decreased appetite')
        X = self.change_func(X, ws = ['skin color change', 'skin colour change'], new = 'skin color change')
        X = self.change_func(X, ws = ['aversion to light', 'anversion to light'], new = 'aversion to light')
        X = self.change_func(X, ws = ['ocular discharge', 'occular discharge','eye discharges', 'eye disharge','discharge from eyes', 'mucus discharge from the eye'], new = 'ocular discharge')
        X = self.change_func(X, ws = ['fluffed feather', 'fluffed feathers'], new = 'fluffed feathers')
        X = self.change_func(X, ws = ['abdominal pain', 'abdminal pain','abdonormal discomfort', 'abdominal discomfort','abdonormal pain', 'abdominal pain'], new = 'abdominal pain')
        X = self.change_func(X, ws = ['inappetence', 'inappentence'], new = 'inappetence')
        X = self.change_func(X, ws = ['skin reashes', 'skin rashes'], new = 'skin rashes')
        X = self.change_func(X, ws = ['nosebleeds', 'nose bleeds', 'nose bleeds', 'nosebleed'], new = 'nose bleeds')
        X = self.change_func(X, ws = ['despression', 'depression'], new = 'depression')
        X = self.change_func(X, ws = ['weightloss', 'weight loss'], new = 'weight loss')
        X = self.change_func(X, ws = ['watery eyes', 'watery eye'], new = 'watery eyes')
        X = self.change_func(X, ws = ['diffulty swallowing', 'difficulty swallowing'], new = 'difficulty swallowing')
        X = self.change_func(X, ws = ['swelling of joints', 'swelling on joints'], new = 'joints swell')
        X = self.change_func(X, ws = ['vomitting', 'vomiting'], new = 'vomit')
        X = self.change_func(X, ws = ['dizzines', 'dizziness'], new = 'dizziness')
        X = self.change_func(X, ws = ['dullness', 'dull ness'], new = 'dullness')
        X = self.change_func(X, ws = ['diarrhea', 'diarrhoea'], new = 'diarrhoea')
        X = self.change_func(X, ws = ['head ache', 'headache', 'head tossing', 'head pressing'], new = 'headache')
        X = self.change_func(X, ws = ['pneumonia', 'pnemonia'], new = 'pneumonia')
        X = self.change_func(X, ws = ['bloody diarrhea', 'bloody diarhhea'], new = 'bloody diarrhoea')
        X = self.change_func(X, ws = ['watery eyes', 'watery eye'], new = 'watery eyes')
        X = self.change_func(X, ws = ['diffulty swallowing', 'difficulty swallowing', 'difficulty in swallowing', 'difficulty swallowing'], new = 'difficulty swallowing')
        X = self.change_func(X, ws = ['abnormalities', 'abnormalalities'], new = 'abnormalities')
        X = self.change_func(X, ws = ['blood in faces', 'blood on faces', 'blood stool', 'blood in stool'], new = 'bloody faces')
        X = self.change_func(X, ws = ['tremor', 'tremors'], new = 'tremor')
        X = self.change_func(X, ws = ['anemia', 'aneamia','anemia', 'anaemia'], new = 'anemia')
        X = self.change_func(X, ws = ['hyperesthesia', 'hyperaestesia'], new = 'hyperesthesia')
        X = self.change_func(X, ws = ['attack', 'attacks'], new = 'attack')
        X = self.change_func(X, ws = ['lesion', 'lesions', 'lession on the skin', 'lession on cat skin'], new = 'lesion')
        X = self.change_func(X, ws = ['excess salivation', 'excession salivation', 'excessive grooming', 'excessive drooling','excess salivation', 'excess salivary'], new = 'excess salivation')
        X = self.change_func(X, ws = ['muscles ache', 'muscle aches'], new = 'muscle ache')
        X = self.change_func(X, ws = ['nausea', 'nause'], new = 'nausea')
        X = self.change_func(X, ws = ['edema', 'oedema'], new = 'edema')
        X = self.change_func(X, ws = ['ulcers', 'ulcer'], new = 'ulcer')
        X = self.change_func(X, ws = ['sweat', 'sweats','sweating'], new = 'sweat')
        X = self.change_func(X, ws = ['grinding teeth', 'grinding of teeth'], new = 'grinding of teeth')
        X = self.change_func(X, ws = ['scratching', 'scartching'], new = 'scratching')
        X = self.change_func(X, ws = ['join pains', 'joint pain'], new = 'joint pain')
        X = self.change_func(X, ws = ['salivating', 'salivation'], new = 'salivation')
        X = self.change_func(X, ws = ['week pulse', 'weak pulse'], new = 'week pulse')
        X = self.change_func(X, ws = ['oains', 'pain', 'pain', 'pains'], new = 'pain')
        X = self.change_func(X, ws = ['shaking oh head', 'shaking head','head shking', 'head shaking'], new = 'head shaking')
        X = self.change_func(X, ws = ['scratches', 'scartches'], new = 'scratching')
        X = self.change_func(X, ws = ['muscle stiffness', 'muscular stiffness'], new = 'muscle stiffness')
        X = self.change_func(X, ws = ['ruffled feathers', 'fluffed feathers','puffed up feather', 'ruffled feathers'], new = 'ruffled feathers')
        X = self.change_func(X, ws = ['seizuers', 'seizures'], new = 'seizures')
        X = self.change_func(X, ws = ['lethargy', 'lathargy'], new = 'lathargy')
        X = self.change_func(X, ws = ['weekness', 'weakness'], new = 'weakness')
        X = self.change_func(X, ws = ['bleeding wounds', 'bleeding from wounds'], new = 'bleeding from wounds')
        X = self.change_func(X, ws = ['gasc', 'gas'], new = 'gas')
        X = self.change_func(X, ws = ['high temperature', 'high body temperature'], new = 'high temperature')
        X = self.change_func(X, ws = ['fatigue', 'fatique'], new = 'fatigue')
        X = self.change_func(X, ws = ['distress', 'stress'], new = 'stress')
        X = self.change_func(X, ws = ['poor coat condition', 'poor condition', 'poor condition', 'poor body condition','poor coat condition', 'poor body condition'], new = 'poor condition')
        X = self.change_func(X, ws = ['relunctance to move', 'reluctant move'], new = 'reluctant move')
        X = self.change_func(X, ws = ['bloody urine', 'blood in urine'], new = 'bloody urine')
        X = self.change_func(X, ws = ['change in gait', 'changed gait'], new = 'change in gait')
        X = self.change_func(X, ws = ['drop in milk production', 'decrease in milk production'], new = 'decrease in milk production')
        X = self.change_func(X, ws = ['thivk skin', 'thicked skin'], new = 'thick skin')
        X = self.change_func(X, ws = ['tear produce', 'tear production'], new = 'tear production')
        X = self.change_func(X, ws = ['rapid heartbeats', 'rapid heart rate'], new = 'rapid heartbeats')
        X = self.change_func(X, ws = ['flock moratality', 'kid moratality'], new = 'flock moratality')
        X = self.change_func(X, ws = ['skin irritation', 'irritation'], new = 'skin irritation')
        X = self.change_func(X, ws = ['itchiness', 'itches', 'itching'], new = 'itches')
        X = self.change_func(X, ws = ['listless', 'listlessness'], new = 'listless')
        X = self.change_func(X, ws = ['drooping wings', 'droopy wings'], new = 'droopy wings')
        X = self.change_func(X, ws = ['tachypea', 'trachea'], new = 'trachea')
        X = self.change_func(X, ws = ['hot joints', 'hock joint'], new = 'hot joints')
        X = self.change_func(X, ws = ['cough', 'coughing'], new = 'cough')
        X = self.change_func(X, ws = ['swelling on thebody'], new = 'swelling on the body')

        return X
