from strap import hostname, pkg, utc

utc()
hostname('strap.example.com')

pkg('fish')
pkg('tmux')
pkg('wireguard', 'wg', {'ppa': 'wireguard/wireguard'})