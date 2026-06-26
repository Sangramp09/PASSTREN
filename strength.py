"""
PasStren - Simplified & Accurate
Predicts password strength with better scoring logic
"""

import re
import math


class PasStren:
    """PasStren password strength analyzer"""

    def __init__(self):
        self.common_passwords = [
            'password', '123456', '12345678', 'qwerty', 'abc123',
            'admin', 'letmein', 'welcome', 'monkey', 'dragon',
            'master', 'hello', 'freedom', 'whatever', 'qazwsx',
            'iloveyou', 'sunshine', 'princess', 'superman', 'football'
        ]

    def analyze(self, password):

        if not password:
            return self._empty_result()

        length = len(password)

        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'[0-9]', password))
        has_special = bool(
            re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?/~`]', password)
        )

        is_common = self._is_common(password)

        score = self._calculate_score(
            length,
            has_lower,
            has_upper,
            has_digit,
            has_special,
            is_common
        )

        return {
            "password": "*" * length,
            "length": length,
            "score": score,
            "rating": self._get_rating(score),
            "strength_bar": self._get_bar(score),

            "good_points": self._get_good_points(
                length,
                has_lower,
                has_upper,
                has_digit,
                has_special,
                is_common
            ),

            "suggestions": self._get_suggestions(
                length,
                has_lower,
                has_upper,
                has_digit,
                has_special,
                is_common
            ),

            "details": {
                "lowercase": has_lower,
                "uppercase": has_upper,
                "digits": has_digit,
                "special": has_special,
                "common_password": is_common
            }
        }

    def _calculate_score(
        self,
        length,
        has_lower,
        has_upper,
        has_digit,
        has_special,
        is_common
    ):

        score = 0

        if length >= 16:
            score += 40
        elif length >= 12:
            score += 30
        elif length >= 8:
            score += 20
        elif length >= 6:
            score += 10
        else:
            score += 5

        char_types = sum([
            has_lower,
            has_upper,
            has_digit,
            has_special
        ])

        if char_types == 4:
            score += 60
        elif char_types == 3:
            score += 45
        elif char_types == 2:
            score += 25
        elif char_types == 1:
            score += 10

        if length >= 12 and char_types >= 3:
            score += 10

        if length >= 16 and char_types >= 4:
            score += 15

        if is_common:
            score -= 50

        return min(100, max(0, score))

    def _get_rating(self, score):

        if score >= 80:
            return "EXCELLENT 🔒"
        elif score >= 60:
            return "STRONG ✅"
        elif score >= 40:
            return "MODERATE ⚠️"
        elif score >= 20:
            return "WEAK ❌"

        return "VERY WEAK 🚨"

    def _get_bar(self, score):

        filled = int(score / 10)

        return (
            "█" * filled +
            "░" * (10 - filled)
        )

    def _get_good_points(
        self,
        length,
        has_lower,
        has_upper,
        has_digit,
        has_special,
        is_common
    ):

        points = []

        if length >= 12:
            points.append(f"✅ Good length ({length})")

        elif length >= 8:
            points.append(f"✅ Acceptable length ({length})")

        if has_lower:
            points.append("✅ Lowercase")

        if has_upper:
            points.append("✅ Uppercase")

        if has_digit:
            points.append("✅ Numbers")

        if has_special:
            points.append("✅ Special characters")

        if not is_common:
            points.append("✅ Not common")

        return points

    def _get_suggestions(
        self,
        length,
        has_lower,
        has_upper,
        has_digit,
        has_special,
        is_common
    ):

        tips = []

        if length < 8:
            tips.append("Use at least 8 characters")

        if not has_upper:
            tips.append("Add uppercase")

        if not has_lower:
            tips.append("Add lowercase")

        if not has_digit:
            tips.append("Add numbers")

        if not has_special:
            tips.append("Add special characters")

        if is_common:
            tips.append("Avoid common passwords")

        return tips or ["🎉 Excellent password"]

    def _is_common(self, password):

        pwd = password.lower()

        if pwd in self.common_passwords:
            return True

        patterns = [
            r'12345',
            r'abcdef',
            r'qwerty',
            r'(.)\1{3,}'
        ]

        return any(
            re.search(
                p,
                pwd
            )
            for p in patterns
        )

    def _empty_result(self):

        return {
            "password": "",
            "length": 0,
            "score": 0,
            "rating": "INVALID",
            "strength_bar": "░░░░░░░░░░",
            "good_points": [],
            "suggestions": ["Enter a valid password"],
            "details": {}
        }

    def display_report(self, result):

        print("\n" + "=" * 60)

        print("              🔐 PASSTREN REPORT")

        print("=" * 60)

        print(f"\nPassword : {result['password']}")
        print(f"Length   : {result['length']}")
        print(f"Score    : {result['score']}/100")
        print(f"Rating   : {result['rating']}")
        print(f"Strength : [{result['strength_bar']}]")

        print("\nGOOD:")
        for p in result["good_points"]:
            print("-", p)

        print("\nSUGGESTIONS:")
        for s in result["suggestions"]:
            print("-", s)


def main():

    analyzer = PasStren()

    print("\n==============================")
    print("      🔐 PASSTREN")
    print("==============================")

    while True:

        pwd = input("\nEnter Password: ").strip()

        if pwd.lower() in ["quit", "exit"]:

            print("\n👋 Exiting PasStren")

            break

        result = analyzer.analyze(pwd)

        analyzer.display_report(result)


if __name__ == "__main__":
    main()