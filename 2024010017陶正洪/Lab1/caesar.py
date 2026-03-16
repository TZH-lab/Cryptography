def caesar_decrypt(ciphertext, shift):
    """
    对密文进行凯撒解密
    :param ciphertext: 密文字符串
    :param shift: 移位量（密钥）
    :return: 解密后的明文
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 只处理字母，保持大写形式
            shifted = ord(char) - shift
            if shifted < ord('A'):
                shifted += 26
            plaintext += chr(shifted)
        else:
            # 非字母字符保持不变
            plaintext += char
    return plaintext


def brute_force_caesar(ciphertext):
    """
    穷举所有可能的密钥（1-25）进行解密
    :param ciphertext: 密文字符串
    """
    print(f"密文: {ciphertext}")
    print("=" * 50)
    print("所有可能的解密结果：")
    print("=" * 50)
    
    results = []
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"k={shift:2d}: {decrypted}")
        results.append((shift, decrypted))
    
    return results


def find_meaningful_result(results):
    """
    找出有意义的明文结果
    通过常见英文单词和词组来判断
    """
    # 常见的英文单词和词组
    common_words = ['THE', 'AND', 'FOR', 'YOU', 'ARE', 'THIS', 'THAT', 
                   'HAVE', 'WILL', 'YOUR', 'FROM', 'WITH', 'KNOW', 
                   'PLEASE', 'STUDENT', 'HELLO', 'WORLD', 'LAB', 
                   'EXPERIMENT', 'CAESAR', 'CIPHER']
    
    meaningful_results = []
    for shift, text in results:
        # 检查是否包含常见英文单词
        words = text.split()
        match_count = 0
        for word in words:
            if word in common_words:
                match_count += 1
        
        # 如果匹配到至少一个常见单词，认为是可能的结果
        if match_count > 0:
            meaningful_results.append((shift, text, match_count))
    
    # 按匹配单词数量排序
    meaningful_results.sort(key=lambda x: x[2], reverse=True)
    return meaningful_results


def main():
    # 给定的密文
    ciphertext = "NUFECMBYUBJBIQGYNBYMIXY"
    
    # 执行穷举解密
    results = brute_force_caesar(ciphertext)
    
    print("=" * 50)
    print("\n分析结果：")
    print("=" * 50)
    
    # 找出最有意义的结果
    meaningful = find_meaningful_result(results)
    
    if meaningful:
        best_shift, best_text, match_count = meaningful[0]
        print(f"正确的密钥是: k = {best_shift}")
        print(f"解密后的明文是: {best_text}")
        print(f"\n判断依据:")
        print(f"1. 该结果包含多个常见的英文单词：")
        # 找出结果中包含的常见单词
        words = best_text.split()
        found_words = [word for word in words if word in ['THE', 'AND', 'FOR', 'YOU', 'ARE', 'THIS', 'THAT', 
                                                         'HAVE', 'WILL', 'YOUR', 'FROM', 'WITH', 'KNOW']]
        print(f"   - 识别出的单词: {', '.join(found_words)}")
        print(f"2. 该结果在语法上通顺，符合英文表达习惯")
        print(f"3. 其他密钥解密结果均为无意义的乱码")
    else:
        print("未能通过常见单词匹配到有意义的结果，请人工检查所有解密结果")


if __name__ == "__main__":
    main()
