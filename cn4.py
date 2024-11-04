import heapq

class LinkStateRouter:
    def __init__(self, name):
        self.name = name
        self.links = {}  # Dictionary of neighbors and their distances

    def add_link(self, neighbor, distance):
        self.links[neighbor] = distance

class LinkStateNetwork:
    def __init__(self):
        self.routers = {}

    def add_router(self, name):
        self.routers[name] = LinkStateRouter(name)

    def add_link(self, router1, router2, distance):
        self.routers[router1].add_link(router2, distance)
        self.routers[router2].add_link(router1, distance)

    def calculate_shortest_paths(self, start):
        # Initialize distances from the start router to all other routers as infinity
        distances = {router: float('inf') for router in self.routers}
        distances[start] = 0

        # Priority queue to track the next router to visit
        pq = [(0, start)]  # (distance, router)

        while pq:
            current_distance, current_router = heapq.heappop(pq)

            # If the current distance is greater than the known distance, skip
            if current_distance > distances[current_router]:
                continue

            # Update distances to neighboring routers
            for neighbor, distance in self.routers[current_router].links.items():
                distance_through_current = current_distance + distance

                # If a shorter path is found, update and push to priority queue
                if distance_through_current < distances[neighbor]:
                    distances[neighbor] = distance_through_current
                    heapq.heappush(pq, (distance_through_current, neighbor))

        return distances

def main_link_state():
    link_state_network = LinkStateNetwork()

    # Get the number of routers
    num_routers = int(input("Enter the number of routers: "))
    for _ in range(num_routers):
        router_name = input("Enter router name: ")
        link_state_network.add_router(router_name)

    # Get the number of links
    num_links = int(input("Enter the number of links: "))
    for _ in range(num_links):
        router1 = input("Enter the first router name: ")
        router2 = input("Enter the second router name: ")
        distance = int(input("Enter the distance between the routers: "))
        link_state_network.add_link(router1, router2, distance)

    # Get the starting router for calculating shortest paths
    start_router = input("Enter the starting router for shortest paths: ")
    shortest_paths = link_state_network.calculate_shortest_paths(start_router)

    # Display the shortest paths from the start router
    print(f"\nShortest paths from {start_router}:")
    for router, distance in shortest_paths.items():
        print(f" To {router}: {distance}")

if __name__ == "__main__":
    print("--- Link State Routing Protocol ---")
    main_link_state()
