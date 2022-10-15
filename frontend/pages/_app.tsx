import '../styles/globals.css'
import type { AppProps } from 'next/app'

function ThemeSong({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}

export default ThemeSong
