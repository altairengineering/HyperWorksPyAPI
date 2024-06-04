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
async function activate(context) {
    console.log('Extension activated');
    context.subscriptions.push(vscode.commands.registerCommand('hw.hyperworks', () => {
        console.log('Command invoked hyperworksapis');
    }));
    const hmmodels = path_1.default.join(context.extensionPath, 'models');
    const simlabmodels = path_1.default.join(context.extensionPath, 'models', 'simlab');
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
        // Get additional source folder paths from settings.json
        const config = vscode.workspace.getConfiguration('HyperWorksAPI');
        let extraSourceFolders = config.get('extraSourceFolders') || [];
        // Set default source folders if no folders are configured
        if (extraSourceFolders.length === 0) {
            extraSourceFolders = [
                hmmodels, simlabmodels
            ];
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
//# sourceMappingURL=extension.js.map