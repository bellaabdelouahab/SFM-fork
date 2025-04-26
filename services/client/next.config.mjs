/** @type {import('next').NextConfig} */


const nextConfig = {
  reactStrictMode: true,
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    domains: ["flagcdn.com", "images.unsplash.com"],
    unoptimized: true,
  },
  experimental: {},
};

export default nextConfig;
