<script>
    import{
        Canvas,
        Scene,
        PerspectiveCamera,
        DirectionalLight,
        AmbientLight,
        BoxBufferGeometry,
        Mesh,
        MeshStandardMaterial,
        WebGLRenderer,
    } from "svelthree";

    let cubeGeometry = new BoxBufferGeometry(1, 1, 1);
    let cubeMaterial = new MeshStandardMaterial();
    let data_json = {"gx": 0, "gy":0 , "gz":0, "ax": 0, "ay":0, "az":0}

    async function getfetch(){
        let response = await fetch("http://192.168.1.24:80/test");
        data_json = await response.json();
        console.log(data_json);
        console.log("test");
        getfetch();
    }
</script>

<Canvas let:sti w={500} h={500}>
    <Scene {sti} let:scene id="scene1" props={{ background: 0xedf2f7 }}>
        <PerspectiveCamera {scene} id="cam1" pos={[0, 0, 3]} lookAt={[0, 0, 0]} />
        <AmbientLight {scene} intensity={1.25} />
        <DirectionalLight {scene} pos={[3, 3, 3]} />

        <Mesh>
            {getfetch}
            {scene}
            geometry={cubeGeometry}
            material={cubeMaterial}
            mat={{ roughness: 0.5, metalness: 0.5, color: 0xff3e00 }}
            pos={[0, 0, 0]}
            rot={[data_json["ax"], data_json["ay"], data_json["az"]]}
            scale={[1, 1, 1]}
        </Mesh>
        <WebGLRenderer>
            {sti}
            sceneId="scene1"
            camId="cam1"
            config={{ antialias: true, alpha: true }} />
        </WebGLRenderer>
    </Scene>

</Canvas>

<button on:click={getfetch}>取得</button>
<p>gx: {data_json["gx"]}</p>
<p>gy: {data_json["gy"]}</p>
<p>gz: {data_json["gz"]}</p>
<p>ax: {data_json["ax"]}</p>
<p>ay: {data_json["ay"]}</p>
<p>az: {data_json["az"]}</p>