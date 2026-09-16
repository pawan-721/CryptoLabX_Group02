import collections

CIPHERTEXT = """
QRBAI UWYOK ILBRZ XTUWL EGXSN VDXWR XMHXY FCGMW
WWSME LSXUZ
MKMFS BNZIF YEIEG RFZRX WKUFA XQEDX DTTHY NTBRJ
LHTAI KOCZX
QHBND ZIGZG PXARJ EDYSJ NUMKI FLBTN HWISW NVLFM
EGXAI AAWSL
FMHXR SGRIG HEQTU MLGLV BRSIL AEZSG XCMHT OWHFM
LWMRK HPRFB
ELWGF RUGPB HNBEM KBNVW HHUEA KILBN BMLHK XUGML
YQKHP RFBEL
EJYNV WSIJB GAXGO TPMXR TXFKI WUALB RGWIE GHWHG
AMEWW LTAEL
NUMRE UWTBL SDPRL YVRET LEEDF ROBEQ UXTHX ZYOZB
XLKAC KSOHN
VWXKS MAEPH IYQMM FSECH RFYPB BSQTX TPIWH GPXQD
FWTAI KNNBX
SIYKE TXTLV BTMQA LAGHG OTPMX RTXTH XSFYG WMVKH
LOIVU ALMLD
LTSYV WYNVW MQVXP XRVYA BLXDL XSMLW SUIOI IMELI
SOYEB HPHNR
WTVUI AKEYG WIETG WWBVM VDUMA EPAUA KXWHK MAUPA
MUKHQ PWKCX
EFXGW WSDDE OMLWL NKMWD FWTAM FAFEA MFZBN WIHYA
LXRWK MAMIK
GNGHJ UAZHM HGUAL YSULA ELYHJ BZMSI LAILH WWYIK
EWAHN PMLBN
NBVPJ XLBEF WRWGX KWIRH XWWGQ HRRXW IOMFY CZHZL
VXNVI OYZCM
YDDEY IPWXT MMSHS VHHXZ YEWNV OAOEL SMLSW KXXFX
STRVI HZLEF
JXDAS FIE
"""

ENGLISH_FREQ = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02360,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}


def clean_ciphertext(text):
    return "".join(
        char.upper()
        for char in text
        if char.isalpha()
    )


def find_repeated_patterns(text, min_length=3):
    patterns = collections.defaultdict(list)

    for length in range(
        min_length,
        len(text) // 2
    ):
        for i in range(
            len(text) - length + 1
        ):
            pattern = text[i:i + length]

            if not patterns[pattern]:

                position = text.find(pattern)

                while position != -1:
                    patterns[pattern].append(position)

                    position = text.find(
                        pattern,
                        position + 1
                    )

    return {
        pattern: positions
        for pattern, positions in patterns.items()
        if len(positions) > 1
    }


def calculate_distances(patterns):
    distances = []

    for positions in patterns.values():

        for i in range(
            len(positions) - 1
        ):
            distances.append(
                positions[i + 1] - positions[i]
            )

    return distances


def find_factors(distances):
    factors = []

    for distance in distances:

        for factor in range(
            2,
            min(distance + 1, 21)
        ):

            if distance % factor == 0:
                factors.append(factor)

    return collections.Counter(factors)


def calculate_ic(text):

    n = len(text)

    if n <= 1:
        return 0

    counts = collections.Counter(text)

    total = 0

    for count in counts.values():
        total += count * (count - 1)

    return total / (n * (n - 1))


def split_into_groups(text, key_length):

    groups = [""] * key_length

    for i, char in enumerate(text):
        groups[i % key_length] += char

    return groups


def kasiski_analysis(text):

    patterns = find_repeated_patterns(text)

    distances = calculate_distances(patterns)

    factors = find_factors(distances)

    if not factors:
        return 1, {1: calculate_ic(text)}

    candidates = [
        factor
        for factor, count
        in factors.most_common(5)
    ]

    best_length = candidates[0]

    best_difference = float("inf")

    ic_scores = {}

    for length in candidates:

        groups = split_into_groups(
            text,
            length
        )

        average_ic = (
            sum(
                calculate_ic(group)
                for group in groups
            )
            / length
        )

        ic_scores[length] = average_ic

        difference = abs(
            average_ic - 0.066
        )

        if difference < best_difference:

            best_difference = difference

            best_length = length

    return best_length, ic_scores


def frequency_analysis(group):

    counts = collections.Counter(group)

    total = len(group)

    frequency = {}

    for i in range(26):

        letter = chr(
            ord('A') + i
        )

        frequency[letter] = (
            counts.get(letter, 0)
            / total
        )

    return frequency


def find_shift(group):

    frequency = frequency_analysis(group)

    best_shift = 0

    best_score = float("inf")

    for shift in range(26):

        score = 0

        for i in range(26):

            cipher_letter = chr(
                ord('A') + i
            )

            plain_letter = chr(
                (
                    i - shift
                ) % 26
                + ord('A')
            )

            observed = frequency[
                cipher_letter
            ]

            expected = ENGLISH_FREQ[
                plain_letter
            ]

            score += (
                (observed - expected) ** 2
            ) / expected

        if score < best_score:

            best_score = score

            best_shift = shift

    return best_shift


def find_key(groups):

    key = ""

    for group in groups:

        shift = find_shift(group)

        key += chr(
            ord('A') + shift
        )

    return key


def vigenere_decrypt(text, key):

    plaintext = ""

    key_index = 0

    for char in text:

        if char.isalpha():

            shift = (
                ord(
                    key[
                        key_index
                        % len(key)
                    ]
                )
                - ord('A')
            )

            plain_char = chr(
                (
                    ord(char.upper())
                    - ord('A')
                    - shift
                ) % 26
                + ord('A')
            )

            plaintext += plain_char

            key_index += 1

    return plaintext


def vigenere_encrypt(text, key):

    ciphertext = ""

    key_index = 0

    for char in text:

        if char.isalpha():

            shift = (
                ord(
                    key[
                        key_index
                        % len(key)
                    ]
                )
                - ord('A')
            )

            cipher_char = chr(
                (
                    ord(char.upper())
                    - ord('A')
                    + shift
                ) % 26
                + ord('A')
            )

            ciphertext += cipher_char

            key_index += 1

    return ciphertext


def verify(
    plaintext,
    key,
    original_ciphertext
):

    encrypted = vigenere_encrypt(
        plaintext,
        key
    )

    return (
        encrypted
        == clean_ciphertext(
            original_ciphertext
        )
    )


def format_freq_table(freq_dict):

    sorted_freq = sorted(
        freq_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_five = sorted_freq[:5]

    return ", ".join(
        f"{letter}: {frequency:.3f}"
        for letter, frequency
        in top_five
    )


if __name__ == "__main__":

    print("=" * 55)
    print("VIGENERE CRYPTANALYSIS")
    print("KASISKI + INDEX OF COINCIDENCE + FREQUENCY")
    print("=" * 55)

    cleaned_ct = clean_ciphertext(
        CIPHERTEXT
    )

    print(
        "\n[*] Ciphertext length:",
        len(cleaned_ct)
    )

    key_length, ic_scores = kasiski_analysis(
        cleaned_ct
    )

    print("\n[*] Kasiski / IC Analysis")

    for length, ic in ic_scores.items():

        print(
            f"    Key Length {length}: "
            f"IC = {ic:.4f}"
        )

    print(
        "\n[+] Estimated Key Length:",
        key_length
    )

    groups = split_into_groups(
        cleaned_ct,
        key_length
    )

    print("\n[*] Frequency Analysis")

    for i, group in enumerate(groups):

        frequency = frequency_analysis(
            group
        )

        print(
            f"    Group {i + 1}: "
            f"{format_freq_table(frequency)}"
        )

    recovered_key = find_key(groups)

    print(
        "\n[+] Recovered Key:",
        recovered_key
    )

    recovered_plaintext = vigenere_decrypt(
        CIPHERTEXT,
        recovered_key
    )

    print("\n[+] Recovered Plaintext")
    print("-" * 55)

    print(
        recovered_plaintext[:100]
        + "..."
    )

    print("-" * 55)

    with open(
        "recovered_plaintext.txt",
        "w"
    ) as file:

        file.write(
            recovered_plaintext
        )

    print(
        "\n[+] Full plaintext saved to "
        "recovered_plaintext.txt"
    )

    print("\n[*] Verifying Recovery...")

    if verify(
        recovered_plaintext,
        recovered_key,
        CIPHERTEXT
    ):

        print(
            "[SUCCESS] Re-encryption "
            "matches original ciphertext."
        )

    else:

        print(
            "[FAILED] Re-encryption "
            "does not match."
        )

    print("\n" + "=" * 55)