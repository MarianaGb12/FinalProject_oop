# %%
import pandas as pd

# %%
class Recomendar:
    def __init__(self, df1:str):
        # cargamos la base de datos en el constructor 
        self.df1 = pd.read_csv('https://drive.google.com/uc?export=download&id=1ak6fsjArzXSFHh0cpycCx58lAJvcrV4Q')
        
        """
          cambiamos los nombres de las categorías
          a íngles para facilitar la comprensión
          de las recomendaciones.
        """ 
        self.df1['categories'] = self.df1['categories'].replace({'Fiction':'Ficción','American fiction':'Ficción',
                                            'Detective and mystery stories':'Policial',
                                            'Christian life':'Lit.cristiana',
                                            'Authors, English':'Informativo',
                                            'Africa, East':'Informativo',
                                            'Hyland, Morn (Fictitious character)':'Ficción',
                                            'Adventure stories':'Aventura',
                                            'Arthurian romances':'Romance',
                                            'Fantasy fiction':'Ficción',
                                            'English drama':'Drama',
                                            'Country life':'Literatura',
                                            'English fiction':'Ficción',
                                            'Clergy':'Literatura',
                                            'Aubrey, Jack (Fictitious character)':'Ficción',
                                            'Detective and mystery stories, English':'Policial',
                                            'Black Death':'Ficción',
                                            'Human cloning':'Literatura',
                                            'Science fiction':'Ficción',
                                            'Great Britain':'Historia',
                                            'American essays':'Informativo',
                                            'China':'Historia',
                                            'Capitalism':'Economia',
                                            'Ireland':'Historia',
                                            'Juvenile Fiction':'Ficción',
                                            "Children's stories, English":'Literatura',
                                            'Male friendship':'Literatura',
                                            'Literary Collections':'Literatura',
                                            'Beresford, Tommy (Fictitious character)':'Ficción',
                                            'Imaginary wars and battles':'Ficción',
                                            'Dysfunctional families':'Psicologia',
                                            'Poirot, Hercule (Fictitious character)':'Ficción',
                                            'Christmas stories':'Literatura',
                                            'Marple, Jane (Fictitious character)':'Ficción',
                                            'Belgians':'Historia',
                                            'Battle, Superintendent (Fictitious character)':'Ficción',
                                            'Baggins, Frodo (Fictitious character)':'Ficción',
                                            'Cambridge (Mass.)':'Historia',
                                            'Business enterprises':'Economia',
                                            'Emotional problems':'Psicologia',
                                            'Characters and characteristics in motion pictures':'Informativo',
                                            'Fantasy fiction, English':'Ficción',
                                            'Fairy tales, English':'Historia',
                                            'Hallucinogenic drugs':'Literatura',
                                            "Children's stories":'Literatura',
                                            'Parenthood':'Literatura',
                                            'Biography & Autobiography':'Informativo',
                                            'Authors, American':'Historia',
                                            'Vietnam War, 1961-1975':'Historia',
                                            'Boys':'Literatura',
                                            'Computer programmers':'Informativo',
                                            'Actors':'Literatura',
                                            'Friendship':'Literatura',
                                            'Authors':'Informativo',
                                            'Costume':'Literatura',
                                            'African American plantation owners':'Informativo',
                                            'Conduct of life':'Informativo',
                                            'Alienation (Social psychology)':'Psicologia',
                                            'Cowboys':'Historia',
                                            'Fairy tales':'Literatura',
                                            'Christianity':'Lit.cristiana',
                                            'Philosophy':'Filosofia',
                                            'Language Arts & Disciplines':'Informativo',
                                            'History':'Historia',
                                            'Animals, Treatment of':'Informativo',
                                            'Grandmothers':'Historia',
                                            'Business & Economics':'Economia',
                                            'Literary Criticism':'Lit.cristiana',
                                            'Science':'Ciencia',
                                            'Family & Relationships':'Psicologia',
                                            'Juvenile Nonfiction':'Psicologia',
                                            'African Americans in radio broadcasting':'Historia',
                                            'Poetry':'Literatura',
                                            'Self-Help':'Psicologia',
                                            'Sports & Recreation':'Recreacion',
                                            'True Crime':'Policial',
                                            'Psychology':'Psicologia',
                                            'Religion':'Lit.cristiana',
                                            'Travel':'Aventura',
                                            'Social Science':'Ciencia',
                                            'Health & Fitness':'Recreacion',
                                            'Music':'Recreacion',
                                            'Comics & Graphic Novels':'Recreacion',
                                            'Political science':'Ciencia',
                                            'Medical':'Ciencia',
                                            'Body, Mind & Spirit':'Psicologia',
                                            'Education':'Informativo',
                                            'Antiques & Collectibles':'Literatura',
                                            'Young Adult Fiction':'Ficción',
                                            'Reference':'Informativo',
                                            'Art':'Informativo',
                                            'Families':'Literatura',
                                            'Humor':'Psicologia',
                                            'Nature':'Informativo',
                                            'Foreign Language Study':'Informativo',
                                            'Computers':'Ciencia',
                                            'Heat':'Literatura',
                                            'Cosmology':'Ciencia',
                                            'Physicists':'Ciencia',
                                            'Australian fiction':'Ficción',
                                            'Australia':'Historia',
                                            'Azerbaijan':'Historia',
                                            'Dublin (Ireland)':'Historia',
                                            'Americans':'Historia',
                                            'Slave insurrections':'Literatura',
                                            'Amis, Kingsley':'Literatura',
                                            'Dangerously mentally ill':'Literatura',
                                            'American literature':'Literatura',
                                            'Life on other planets':'Ficción',
                                            'Anger':'Literatura',
                                            'Comedy':'Recreacion',
                                            "Alzheimer's disease":'Psicologia',
                                            'College teachers':'Informativo',
                                            'Essays':'Literatura',
                                            'Mothers and sons':'Recreacion',
                                            'Atonement':'Literatura',
                                            'Badgers':'Literatura',
                                            'Human behavior':'Informativo',
                                            'Gangs':'Literatura',
                                            'Social action':'Psicologia',
                                            'Horror':'Terror',
                                            'Galicia (Spain : Region)':'Informativo',
                                            'Businesswomen':'Economia',
                                            'Domestic fiction':'Ficción',
                                            'Japan':'Historia',
                                            'Crime investigation':'Policial',
                                            'Authors, German':'Informativo',
                                            'Short stories, American':'Historia',
                                            'Short stories':'Historia',
                                            'African Americans':'Hsitoria',
                                            'Exorcism':'Terror',
                                            'Europe':'Historia',
                                            'Horror tales':'Terror',
                                            'Cults':'Informativo',
                                            'Divorced women':'Drama',
                                            'Bracelets':'Informativo',
                                            'Death':'Terror',
                                            'Egyptologists':'Historia',
                                            'Demonology':'Informativo',
                                            'Alcoholics':'Informativo',
                                            'Feature films [DVD]':'Recreacion',
                                            'Brothers':'Literatura',
                                            'England':'Historia',
                                            'Adultery':'Psicologia',
                                            'Accidents':'Informativo',
                                            'Christmas':'Literatura',
                                            'World War, 1914-1918':'Historia',
                                            'College attendance':'Literatura',
                                            'London (England)':'Historia',
                                            'Children of the rich':'Literatura',
                                            'Literature':'Literatura',
                                            'City and town life':'Literatura',
                                            'Classical fiction':'Ficción',
                                            'War':'Historia',
                                            'Historical fiction':'Ficción',
                                            'Igbo (African people)':'Informativo',
                                            'Law':'Literatura',
                                            'Mathematics':'Ciencia',
                                            'Ghost stories, American':'Historia',
                                            'Autobiographical fiction':'Ficción',
                                            'Pigeons':'Literatura',
                                            'Electrons':'Informativo',
                                            'Existential psychotherapy':'Psicologia',
                                            'Albigenses':'Informativo',
                                            'Sex':'Informativo',
                                            'Child analysis':'Psicologia',
                                            'Tobruk, Battles of, 1941-1942':'Historia',
                                            'Latin America':'Historia',
                                            'Drama':'Drama',
                                            'Confucianism':'Filosofia',
                                            'Performing Arts':'Informativo',
                                            'British':'Historia',
                                            'English':'Informativo',
                                            'Humorous stories, English':'Recreacion',
                                            'Authors, Italian':'Historia',
                                            'Canadian wit and humor':'Recreacion',
                                            'Obesity':'Informativo',
                                            'High schools':'Informativo',
                                            'English poetry':'Literatura',
                                            'Amour - Ouvrages avant 1800':'Romance',
                                            'Candy':'Informativo',
                                            'Courtship':'Literatura',
                                            'Dracula, Count (Fictitious character)':'Terror',
                                            'Bond, James (Fictitious character)':'Ficción',
                                            'Dead':'Literatura',
                                            'Cabrillo, Juan (Fictitious character)':'Ficción',
                                            'Cookery':'Literatura',
                                            'Jews':'Literatura',
                                            'Children of Holocaust survivors':'Historia',
                                            'American wit and humor':'Recreacion',
                                            'Experimental fiction, American':'Ficción',
                                            'Argentine literature':'Literatura',
                                            'Novelists, American':'Literatura',
                                            'Men':'Literatura',
                                            'Czechoslovakia':'Historia',
                                            'French drama':'Drama',
                                            'Epidemics':'Informativo',
                                            'Repression (Psychology)':'Psicologia',
                                            'Horror tales, American':'Terror',
                                            'Mentally ill':'Psicologia',
                                            'Handicapped youth':'Literatura',
                                            'Sea monsters':'Terror',
                                            'Mysticism':'Terror',
                                            'Book burning':'Literatura',
                                            'Spiritual life':'Lit.cristiana',
                                            'Comic books, strips, etc':'Recracion',
                                            'Cooking':'Recreacion',
                                            'Existentialism':'Filosofia',
                                            'Bedtime':'Literatura',
                                            'Games':'Recreacion',
                                            'Germany':'Historia',
                                            'Aircraft accidents':'Informativo',
                                            'Study Aids':'Informativo',
                                            'Leadership':'Informativo',
                                            'Crusades':'Historia',
                                            'Intellectual disability facilities':'Psicolgia',
                                            'Comic books, strips, etc':'Recracion',
                                            'Indic fiction (English)':'Ficción',
                                            'Political Science':'Ciencia'})

    def recom_populares(self, x=0):
        """ 
        Recomendación por popularidad. 
        Recomienda al usuario libros 
        que tienen entre 3 y 5 estrellas
        """
        
        x = 0
        self.df1 = self.df1.sort_values('average_rating',ascending=False)
        self.df1 = self.df1.drop(['subtitle','description','isbn13','isbn10','num_pages','ratings_count','thumbnail'], axis=1)

        if x == 0:
            self.df1 = self.df1[self.df1.average_rating >3]
            self.df1 = self.df1[self.df1.average_rating <=5]
        return self.df1

    
# %%
view = Recomendar("")
view.recom_populares()
# %%
