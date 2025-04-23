"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const path_1 = __importDefault(require("path"));
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("fs"));
async function activate(context) {
    console.log('Extension activated');
    context.subscriptions.push(vscode.commands.registerCommand('hw.hyperworks', () => {
        console.log('Command invoked hyperworksapis');
    }));
    // Path to directory with the python files
    const models = path_1.default.join(context.extensionPath, 'models');
    // Check if Python is installed
    const pythonExtension = vscode.extensions.getExtension('ms-python.python');
    if (!pythonExtension) {
        const pythonChoice = await vscode.window.showInformationMessage('This extension requires Python to provide enhanced features. Would you like to install Python now?', 'Yes', 'No');
        if (pythonChoice === 'Yes') {
            vscode.commands.executeCommand('workbench.extensions.installExtension', 'ms-python.python');
        }
    }
    // Check if Pylance is installed
    const pylanceExtension = vscode.extensions.getExtension('ms-python.vscode-pylance');
    if (!pylanceExtension) {
        const pylanceChoice = await vscode.window.showInformationMessage('This extension requires Pylance to provide enhanced features. Would you like to install Pylance now?', 'Yes', 'No');
        if (pylanceChoice === 'Yes') {
            vscode.commands.executeCommand('workbench.extensions.installExtension', 'ms-python.vscode-pylance');
        }
    }
    else {
        try {
            // Get the user settings file path
            const settingsPath = getSettingsFilePath();
            if (!fs.existsSync(settingsPath)) {
                vscode.window.showErrorMessage(`Settings file not found: ${settingsPath}`);
                return;
            }
            // Read and parse settings.json
            const settingsData = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));
            // Specify keys to remove
            const keysToRemove = ['python.analysis.extraPaths', 'HyperWorksAPI.extraSourceFolders']; // Replace with your keys
            let keysRemoved = 0;
            const elementsToRemove = ['/models', '\\models'];
            // Remove specified keys if they exist
            for (const key of keysToRemove) {
                if (key in settingsData) {
                    if (key === 'python.analysis.extraPaths') {
                        settingsData[key] = settingsData[key].filter((item) => !elementsToRemove.includes(item));
                    }
                    else {
                        delete settingsData[key];
                        keysRemoved++;
                    }
                }
            }
            if (keysRemoved > 0) {
                // Write updated settings back to settings.json
                fs.writeFileSync(settingsPath, JSON.stringify(settingsData, null, 4), 'utf-8');
                vscode.window.showInformationMessage(`Removed ${keysRemoved} keys from settings.json!`);
            }
            else {
                vscode.window.showInformationMessage('No specified keys were found in settings.json.');
            }
        }
        catch (error) {
            const errorMessage = error instanceof Error ? error.message : String(error);
            vscode.window.showErrorMessage(`Error: ${errorMessage}`);
        }
        // Get additional source folder paths from settings.json
        const config = vscode.workspace.getConfiguration('HyperWorksAPI');
        let extraSourceFolders = config.get('extraSourceFolders') || [];
        // Set default source folders if no folders are configured
        if (extraSourceFolders.length === 0) {
            extraSourceFolders.push(models);
            // Save default source folders to settings.json
            await config.update('extraSourceFolders', extraSourceFolders, vscode.ConfigurationTarget.Global);
        }
        // Include Python files from additional source folders in analysis
        const pylanceConfig = vscode.workspace.getConfiguration('python.analysis');
        let extraPaths = pylanceConfig.get('extraPaths') || [];
        for (const folder of extraSourceFolders) {
            const folderUri = vscode.Uri.file(folder);
            const folderExists = await isFolderExists(folderUri);
            if (folderExists) {
                extraPaths.push(folderUri.fsPath);
            }
        }
        //Removing Duplicates 
        let extraPathset = new Set(extraPaths);
        extraPaths = [...extraPathset];
        // Update the configuration
        pylanceConfig.update('extraPaths', extraPaths, vscode.ConfigurationTarget.Global);
    }
}
exports.activate = activate;
async function isFolderExists(uri) {
    try {
        const stat = await vscode.workspace.fs.stat(uri);
        return stat.type === vscode.FileType.Directory;
    }
    catch (error) {
        return false;
    }
}
// Get the platform-specific path to settings.json
function getSettingsFilePath() {
    const appDataPath = process.platform === 'win32'
        ? process.env.APPDATA
        : process.platform === 'darwin'
            ? path_1.default.join(process.env.HOME || '', 'Library/Application Support')
            : path_1.default.join(process.env.HOME || '', '.config');
    return path_1.default.join(appDataPath || '', 'Code', 'User', 'settings.json');
}
//# sourceMappingURL=extension.js.map