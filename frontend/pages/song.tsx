import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import MusicPlayer from "../components/MusicPlayer";

const Song: NextPage = () => {
    return (
        <div className={styles.container}>
            <Head>
                <title>Theme Song</title>
                <meta name="description" content="Generated by create next app" /> // TODO description
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className={styles.main}>
                <h2 className={styles.title}>
                    Your song of the day is...
                </h2>

                <p className={styles.description}>
                    <MusicPlayer
                        uri="79dL7FLiJFOO0EoehUHQBv"
                        dark={true}
                    />
                </p>
            </main>

            <footer className={styles.footer}>
                <a
                    href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Powered by{' '}
                    <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
                </a>
            </footer>
        </div>
    )
}

export default Song
