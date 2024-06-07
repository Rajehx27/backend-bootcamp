import random

materials = ["mat1", "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10", "mat11", "mat12",
             "mat13", "mat14", "mat15", "mat16", "mat17", "mat18", "mat19", "mat20"]

alien_delegations = [
    {"name": "Neptunes", "needed_materials": random.sample(materials, 3), "suggestions_num": 5},
    {"name": "Martians", "needed_materials": random.sample(materials, 3), "suggestions_num": 6},
    {"name": "Mooners", "needed_materials": random.sample(materials, 3), "suggestions_num": 3},
    {"name": "Venusians", "needed_materials": random.sample(materials, 3), "suggestions_num": 4},
]


def negotiate(delegation):
    print(f"starting negotiating with {delegation['name']}")
    for i in range(delegation["suggestions_num"]):
        suggestion = random.choice(materials)
        print(f"suggestion {i+1}: {suggestion}")
        if suggestion in delegation["needed_materials"]:
            print(f" {delegation['name']} agreed to cooperate with you")
            return True
        else:
            print(f" {delegation['name']} did not agree")
    return False

# negotiate with all delegations
results = []
for delegation in alien_delegations:
    res = negotiate(delegation)
    results.append({"name": delegation["name"], "result": res})


# calculate the success rate
successful_negotiations = sum(1 for res in results if res["result"])
success_rate = successful_negotiations / len(alien_delegations) * 100


for res in results:
    result = "success" if res['result'] else "failed"
    print(f"{res['name']}: {result}")
print(f"success rate: {success_rate}%")
if success_rate >= 70:
    print("Congrats!, you have successfully created new galactic empire")
else:
    print("Sorry, you failed to create new galactic empire")

