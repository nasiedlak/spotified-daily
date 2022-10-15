// @ts-ignore
import SpotifyPlayer from 'react-spotify-player'

const MusicPlayer = (props: { uri: string, dark: boolean }) => {
    return (
        <div className="MusicPlayer">
            <SpotifyPlayer
                uri={`spotify:album:${props.uri}`}
                size={{ width: '100%', height: 300 }}
                view="coverart"
                theme={props.dark ? "black" : "white"}
            />
        </div>
    )
}

export default MusicPlayer
