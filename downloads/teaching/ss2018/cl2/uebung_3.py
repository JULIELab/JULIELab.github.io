import math
import sys

import nltk
from nltk.corpus import brown


class ProbabilityEstimator:

    def __init__(self, bigram_iterable):
        self.bigram_counts = {}  # absolute count of each bigram
        self.unigram_counts = {}  # absolute count of each unigram (count of first token in each bigram)
        self.vocabulary = set()  # vocabulary set
        self.update_counts(bigram_iterable)

    def vocabulary_size(self):
        return len(self.vocabulary)

    def update_counts(self, bigram_iterable):
        """
        Updates bigram counts, unigram counts and the vocabulary.

        :param bigram_iterable: imagine this as a list of bigrams (where each bigram is a tuple)
        """
        for bigram in bigram_iterable:
            # TODO: update counts
            raise NotImplementedError
            self.vocabulary.add(bigram[0])

    def mle_probability(self, w2, w1):
        """
        Returns conditional probability P_mle(w2|w1) using Maximum Likelihood Estimation (MLE).

        :param w2: second word
        :param w1: first word
        :return: MLE probability
        """
        # TODO: compute probability
        raise NotImplementedError

    def smoothed_probability(self, w2, w1, delta):
        """
        Returns conditional probability P_add(w2|w1) with additive smoothing.

        :param w2: second word
        :param w1: first word
        :param delta: smoothing parameter (added constant)
        :return: smoothed probability
        """
        # TODO: compute probability
        raise NotImplementedError


def compute_perplexity(prob_estimator, delta, test_bigrams):
    """
    Returns the perplexity of the model on the test set.

    :param prob_estimator: trained model
    :param delta: smoothing parameter
    :param test_bigrams: bigrams of the test set
    :return: perplexity value
    """
    # TODO: compute perplexity
    raise NotImplementedError


def compare_deltas(prob_estimator, train_size, deltas):
    min_perplexity = sys.float_info.max
    min_perplexity_ind = 0
    for i in range(len(deltas)):
        perplexity = compute_perplexity(prob_estimator, deltas[i], nltk.bigrams(brown.words()[train_size:]))
        if perplexity < min_perplexity:
            min_perplexity = perplexity
            min_perplexity_ind = i
        print('delta={}: {}'.format(deltas[i], perplexity))
    return deltas[min_perplexity_ind]


def compute_prob(prob_estimator, delta, tokens):
    """
    Returns probability of tokens given first order Markov model.

    :param prob_estimator: our trained Markov model
    :param delta: smoothing parameter
    :param tokens: list of tokens (strings)
    :return: estimated probability
    """
    # TODO: compute probability
    raise NotImplementedError


if __name__ == '__main__':
    train_size = 700000  # number of words in training corpus

    print('Counting unigrams and bigrams...')
    prob_estimator = ProbabilityEstimator(nltk.bigrams(brown.words()[:train_size]))
    assert prob_estimator.unigram_counts['the'] == 39416
    assert prob_estimator.bigram_counts[('the', 'president')] == 17
    print()

    print('Comparing perplexity for different deltas...')
    delta = compare_deltas(prob_estimator, train_size, [1, 0.1, 0.001, 0.00001])
    print('--------------------------------------------')
    print('Best delta: {}\n'.format(delta))
    assert delta == 0.001

    print('Computing probability for example sentences...')
    prob_grammatical = compute_prob(prob_estimator, delta, 'the president signed an executive order'.split(' '))
    prob_ungrammatical = compute_prob(prob_estimator, delta, 'president the signed an executive order'.split(' '))
    print('Probability grammatical sentence: {}'.format(prob_grammatical))
    print('Probability ungrammatical sentence: {}'.format(prob_ungrammatical))
    assert prob_grammatical > prob_ungrammatical
