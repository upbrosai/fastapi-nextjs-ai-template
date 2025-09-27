export default {
    input: "./openapi.json",
    output: "src/lib/api-client",
    plugins: [
        // 基础插件配置
        "@hey-api/typescript",
        "@hey-api/sdk",
    ],
    client: "@hey-api/client-axios",
}