from strap import hostname, pkg


hostname('strap.example.com')

pkg('fish')
pkg('tmux')
pkg('wireguard', 'wg', {'ppa': 'wireguard/wireguard'})