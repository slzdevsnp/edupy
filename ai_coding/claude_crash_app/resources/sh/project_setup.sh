#!/bin/bash

# File: project-setup.sh
# This script sets up the directory structure and stub files for the AI Content Generator Tool
# run it from project source folder  e.g  ./resources/sh/project_setup.sh

rm -rf  ai-content-generator
# Create main project directory
mkdir ai-content-generator
cd ai-content-generator

# Create root level files
touch README.md  .gitignore 

# Create src directory structure
mkdir -p src/{app,components,lib,utils}

touch src/package.json src/next.config.js

# Create app subdirectories and files
mkdir -p src/app/{api,project/\[id\]/{upload,config,run,results}}
touch src/app/layout.tsx src/app/page.tsx
touch src/app/api/route.ts
touch src/app/project/page.tsx
touch src/app/project/\[id\]/page.tsx
touch src/app/project/\[id\]/upload/page.tsx
touch src/app/project/\[id\]/config/page.tsx
touch src/app/project/\[id\]/run/page.tsx
touch src/app/project/\[id\]/results/page.tsx

# Create component files
touch src/components/{ProjectList,VideoUploader,PromptConfig,JobStatus,ResultsDisplay}.tsx

# Create lib files
touch src/lib/{db,uploadthing}.ts

# Create utils file
touch src/utils/ai-processing.ts

mkdir database

# Create database file
touch database/schema.ts

# Create flask-backend directory and files
mkdir flask-backend
touch flask-backend/{app.py,requirements.txt}

# Populate stub files with basic content

# Root level files
echo "# AI Content Generator" > README.md
echo "{
  \"name\": \"ai-content-generator\",
  \"version\": \"1.0.0\",
  \"private\": true
}" > src/package.json
echo "node_modules/
.next/
.env" > .gitignore
echo "/** @type {import('next').NextConfig} */
const nextConfig = {
  // Add your Next.js configuration here
}

module.exports = nextConfig" > src/next.config.js

# App files
cat << EOF > src/app/layout.tsx
// File: src/app/layout.tsx
import React from 'react';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
EOF

cat << EOF > src/app/page.tsx
// File: src/app/page.tsx
import React from 'react';

export default function Home() {
  return (
    <div>
      <h1>AI Content Generator</h1>
      {/* TODO: Implement home page content */}
    </div>
  );
}
EOF

# Component files
for component in ProjectList VideoUploader PromptConfig JobStatus ResultsDisplay; do
cat << EOF > src/components/${component}.tsx
// File: src/components/${component}.tsx
import React from 'react';

export default function ${component}() {
  return (
    <div>
      <h2>${component}</h2>
      {/* TODO: Implement ${component} component */}
    </div>
  );
}
EOF
done

# Lib files
echo "// File: src/lib/db.ts
// TODO: Implement database connection and operations" > src/lib/db.ts

echo "// File: src/lib/uploadthing.ts
// TODO: Implement file upload functionality" > src/lib/uploadthing.ts

# Utils file
echo "// File: src/utils/ai-processing.ts
// TODO: Implement AI processing functions" > src/utils/ai-processing.ts

# Database file
echo "// File: src/database/schema.ts
// TODO: Define database schema" > src/database/schema.ts

# Flask backend files
cat << EOF > flask-backend/app.py
# File: flask-backend/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
EOF

echo "flask==2.0.1
# Add other dependencies as needed" > flask-backend/requirements.txt

echo "Project structure created successfully!"