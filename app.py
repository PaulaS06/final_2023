from analyzer.model.adn import ADNAnalyzer, LengthCondition, GCContentCondition, ATGPresenceCondition, \
    CTAPresenceCondition

if __name__ == '__main__':
    analyzer = ADNAnalyzer("assets/data.txt")
    analyzer.add_condition(LengthCondition(50))
    analyzer.add_condition(GCContentCondition(60))
    analyzer.add_condition(ATGPresenceCondition())
    analyzer.add_condition(CTAPresenceCondition())
    print(analyzer.analyze())