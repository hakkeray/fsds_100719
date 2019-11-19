"""A collection of convenient csv urls and sklearn datasets as dataframes."""
def load_data(*args,**kwargs):
    raise Exception('load_data() has been replaced by individual load functions. i.e. fs.datasets.load_boston()')


def read_csv_from_url(url,verbose=False,read_csv_kwds=None):
    """Loading function to load all .csv datasets.
    Args:
        url (str): csv raw link
        verbose (bool): Controls display of loading message and .head()
        read_csv_kwds (dict): dict of commands to feed to pd.read_csv()
    Returns:
        df (DataFrame): the dataset("""
    import pandas as pd
    from sklearn import datasets
    from IPython.display import display
    ## Load and return dataset
    # if verbose: 
        # print(f"[i] Loading {dataset} from url:\n{url}")
    if read_csv_kwds is not None:
        df = pd.read_csv(url,**read_csv_kwds)
    else:
        df = pd.read_csv(url)
    if verbose:
        display(df.head())
    return df


def load_heroes_info(verbose=False,read_csv_kwds=None):
    url = 'https://raw.githubusercontent.com/jirvingphd/dsc-data-cleaning-project-online-ds-ft-100719/master/heroes_information.csv'
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)
    

def load_heroes_powers(verbose=False,read_csv_kwds=None):
    url = "https://raw.githubusercontent.com/learn-co-students/dsc-data-cleaning-project-online-ds-ft-100719/master/super_hero_powers.csv"
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)

def load_titanic(verbose=False,read_csv_kwds=None):
    url ="https://raw.githubusercontent.com/jirvingphd/dsc-dealing-missing-data-lab-online-ds-ft-100719/master/titanic.csv"
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)


def load_mod1_proj(verbose=False,read_csv_kwds=None):
    url = "https://raw.githubusercontent.com/learn-co-students/dsc-v2-mod1-final-project-online-ds-ft-100719/master/kc_house_data.csv"
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)
        

def load_population(verbose=False,read_csv_kwds=None):
    url = "https://raw.githubusercontent.com/learn-co-students/dsc-subplots-and-enumeration-lab-online-ds-ft-100719/master/population.csv"
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)

def load_autompg(verbose=False,read_csv_kwds=None):
    url = 'https://raw.githubusercontent.com/jirvingphd/dsc-dealing-with-categorical-variables-online-ds-ft-100719/master/auto-mpg.csv'
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)




def load_boston(verbose=False):
    
    ## Load Sklearn Datasets
    from sklearn import datasets
    import pandas as pd 
    
    if verbose:
        print("[i] Loading boston housing dataset from sklearn.datasets")
    ## load data dict
    data_dict =  datasets.load_boston()
    # load features
    df_features = pd.DataFrame(data_dict['data'],columns=data_dict['feature_names'])
    # load targets]
    df_features['price'] =data_dict['target']
    
    # set output df
    df = df_features
    if verbose:
        print(data_dict['DESCR'])
    
    return df 

def load_iris(verbose=False):
    from sklearn import datasets
    import pandas as pd
    if verbose:
        print('[i] Loading iris datset from sklearn.datasets')
    data_dict =  datasets.load_iris()
    
    # Get dataframe
    df_features = pd.DataFrame(data_dict['data'],columns=data_dict['feature_names'])
    df_features['target'] = data_dict['target']


    # Get mapper for target names
    iris_map = dict(zip( 
        list(set(data_dict['target'])),
        data_dict['target_names'])
                )
    df_features['target_name']=df_features['target'].map(iris_map)
    df = df_features
    if verbose:
        print(data_dict['DESCR'])   
    return df


def load_height_weight(verbose=False,read_csv_kwds=None):
    """Loads height vs weight dataset"""
    url='https://raw.githubusercontent.com/jirvingphd/dsc-probability-density-function-online-ds-ft-100719/master/weight-height.csv'
    return  read_csv_from_url(url, verbose=verbose,read_csv_kwds=read_csv_kwds)
