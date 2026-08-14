const MainContent = () => {
    return (
        <div className="main-content">
            <h1 className="main-title">
                Read everything<br/>
                Understand anything
            </h1>
            <p className="description">AI-powered explanations layered directly onto your text.<br/>No switching tabs, no lost context.</p>
            <textarea className="text-input" placeholder="Paste a complex article or technical paper here. Click any word to understand it instantly."/>
        </div>
    )
}

export default MainContent