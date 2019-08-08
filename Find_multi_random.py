# Parse every 6 character


def remove_element(num1, num2, num3, num4, num5):
    num_result = list()
    for i in range(len(num1)):
        if num1[i] == num2[i] == num3[i] == num4[i] == num5[i]:
            num_result.append(num1[i])
            i += 1
            print(i)
        else:
            i += 1
    return num_result


if __name__ == "__main__":
    num1 = 'a14806c41500970c39c40320641d55a10791230f69e56074516041168960b46121d28062197e72571835c81813e89680'
    num2 = 'a81864c70594992c91c14317650d95a43734214f04e40053553021110993b98166d48044192e74535832c34840e09609'
    num3 = 'a12812c15545915c59c58395693d80a40726244f23e20090585087161992b70183d22057188e28598848c89806e13651'
    num4 = 'a41871c03523956c39c82397696d51a03717292f94e29042531005178908b91161d97023146e80577839c47894e11676'
    num5 = 'a84898c55540977c51c51352610d07a49774281f96e45071582026122904b95121d19077100e57550827c08810e84688'

    list1 = remove_element(num1, num2, num3, num4, num5)
    str1 = ''.join(list1)
    print(str1)