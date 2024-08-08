import path from 'path';
import * as vscode from 'vscode';

export async function activate(context: vscode.ExtensionContext) {
    console.log('Extension activated');
    context.subscriptions.push(
        vscode.commands.registerCommand('hw.hyperworks', () => {
            console.log('Command invoked hyperworksapis');
        })
    );
	const models = path.join(context.extensionPath, 'models');    
    // Check if Python is installed
    const pythonExtension = vscode.extensions.getExtension('ms-python.python');
    if (!pythonExtension) {
        const pythonChoice = await vscode.window.showInformationMessage(
            'This extension requires Python to provide enhanced features. Would you like to install Python now?',
            'Yes', 'No'
        );

        if (pythonChoice === 'Yes') {
            vscode.commands.executeCommand('workbench.extensions.installExtension', 'ms-python.python');
        }
    }

    // Check if Pylance is installed
    const pylanceExtension = vscode.extensions.getExtension('ms-python.vscode-pylance');
    if (!pylanceExtension) {
        const pylanceChoice = await vscode.window.showInformationMessage(
            'This extension requires Pylance to provide enhanced features. Would you like to install Pylance now?',
            'Yes', 'No'
        );

        if (pylanceChoice === 'Yes') {
            vscode.commands.executeCommand('workbench.extensions.installExtension', 'ms-python.vscode-pylance');
        }
    } else {

        // Get additional source folder paths from settings.json
        const config = vscode.workspace.getConfiguration('HyperWorksAPI');
        let extraSourceFolders: string[] = config.get('extraSourceFolders') || [];

        // Set default source folders if no folders are configured
        if (extraSourceFolders.length === 0) {
            extraSourceFolders = [
                models
            ];

            // Save default source folders to settings.json
            await config.update('extraSourceFolders', extraSourceFolders, vscode.ConfigurationTarget.Global);
        }

        // Include Python files from additional source folders in analysis
        const pylanceConfig = vscode.workspace.getConfiguration('python.analysis');
        let extraPaths = pylanceConfig.get<string[]>('extraPaths') || [];

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

async function isFolderExists(uri: vscode.Uri): Promise<boolean> {
    try {
        const stat = await vscode.workspace.fs.stat(uri);
        return stat.type === vscode.FileType.Directory;
    } catch (error) {
        return false;
    }
}
