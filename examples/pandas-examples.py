import pandas

df = pandas.read_csv('../data.csv')
print(type(df.word))                                        # <class 'pandas.core.series.Series'>
print(df.word)                                              # 0                 is part of theme
                                                            # 1        abandoned industrial site
                                                            # ...
                                                            # 60250           assumption of Mary
                                                            # 60251                 auscultation
                                                            # Name: word, Length: 60252, dtype: object

# df['the words'] in case of whitespace in the name

acid_rain = df.loc[df.word == 'acid rain']                  # filter one record
print(type(acid_rain))                                      # <class 'pandas.core.frame.DataFrame'>
print(acid_rain)                                            #          word                       definition
                                                            # 12  acid rain  Rain having a pH less than 5.6.

acid_rain_definition = df.loc[df.word == 'acid rain'].definition
#                    -   OR   -
acid_rain_definition = df.loc[
                        df['word'] == 'acid rain'
                    ]['definition']
print(type(acid_rain_definition))                           # <class 'pandas.core.series.Series'>
print(acid_rain_definition)

acid_tuple = tuple(acid_rain_definition)
print(acid_tuple)

acid = df.loc[df.word == 'acid']
acid_definition = df.loc[df.word == 'acid'].definition
acid_tuple = tuple(acid_definition)
print(acid_tuple)                                           # ('A compound capable of transferring a hydrogen ion in solution.',
                                                            # 'Being harsh or corrosive in tone.',
                                                            # 'Having an acid, sharp or tangy taste.',
                                                            # 'A powerful hallucinogenic drug manufactured from lysergic acid.',
                                                            # 'Having a pH less than 7, or being sour, or having the strength to neutralize  alkalis, or turning a litmus paper red.')
