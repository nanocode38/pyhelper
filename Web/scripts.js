//// 创建优化的粒子背景
//function createParticles() {
//    const particlesContainer = document.getElementById('particles');
//    const particleCount = 40; // 减少粒子数量减轻负担
//
//    for (let i = 0; i < particleCount; i++) {
//        const particle = document.createElement('div');
//        particle.classList.add('particle');
//
//        // 随机大小、位置和动画时间
//        const size = Math.random() * 6 + 2;
//        const posX = Math.random() * 100;
//        const duration = Math.random() * 15 + 15;
//        const delay = Math.random() * 5;
//
//        particle.style.width = `${size}px`;
//        particle.style.height = `${size}px`;
//        particle.style.left = `${posX}%`;
//        particle.style.bottom = `-${size}px`;
//        particle.style.animationDuration = `${duration}s`;
//        particle.style.animationDelay = `${delay}s`;
//
//        particlesContainer.appendChild(particle);
//    }
//}
//
//// 初始化页面
//window.onload = function() {
//    createParticles();
//};
// Create optimized particle background
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    const particleCount = 50; // Optimal number for performance

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');

        // Random properties
        const size = Math.random() * 5 + 2; // 2-7px
        const posX = Math.random() * 100;
        const duration = Math.random() * 20 + 10; // 10-30s
        const delay = Math.random() * 5;
        const opacity = Math.random() * 0.2 + 0.1; // 0.1-0.3

        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${posX}%`;
        particle.style.bottom = `-${size}px`;
        particle.style.opacity = opacity;
        particle.style.animationDuration = `${duration}s`;
        particle.style.animationDelay = `${delay}s`;

        particlesContainer.appendChild(particle);
    }
}

// Initialize page
window.addEventListener('DOMContentLoaded', () => {
    createParticles();
});