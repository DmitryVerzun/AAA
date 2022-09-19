from typing import List


class CountVectorizer:
    """Implements count vectorizer class

    Methods
    fit_transform(corpus)
        Computes document-term matrix from a list of phrases
        
     get_feature_names()
        Returns the list of feature names, provided 
        fit_transform has already been called"""

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        matrix = []
        self.corpus = [phrase.lower() for phrase in corpus]
        feature_names = self.get_feature_names()

        row = []
        for phrase in self.corpus:
            for feature in feature_names:
                row.append(phrase.count(feature))
            matrix.append(row)
            row = []
        
        return matrix

    def get_feature_names(self) -> List[str]:
        feature_names = []

        for phrase in self.corpus:
            for word in phrase.split():
                if word not in feature_names:
                    feature_names.append(word)

        return feature_names


if __name__ == "__main__":
    corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
