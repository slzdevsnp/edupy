import React from 'react';
import Link from 'next/link';
import { ArrowRight } from 'lucide-react';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center">
      <main>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
              <span className="block">Welcome to</span>
              <span className="block text-rose-500">AI Content Automation</span>
            </h1>
            <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
              Transform your video content into engaging social media posts across multiple platforms with the power of AI.
            </p>
            <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
              <div className="rounded-md shadow">
                <Link href="/projects" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-rose-500 hover:bg-rose-600 md:py-4 md:text-lg md:px-10">
                  Get started
                  <ArrowRight className="ml-2 -mr-1 h-5 w-5" aria-hidden="true" />
                </Link>
              </div>
              <div className="mt-3 rounded-md shadow sm:mt-0 sm:ml-3">
                <Link href="/about" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-rose-500 bg-white hover:bg-gray-50 md:py-4 md:text-lg md:px-10">
                  Learn more
                </Link>
              </div>
            </div>
          </div>
        </div>
      </main>
      <footer className="mt-8 text-center">
        <p className="text-base text-gray-400">
          © 2024 AI Content Automation. All rights reserved.
        </p>
      </footer>
    </div>
  );
}