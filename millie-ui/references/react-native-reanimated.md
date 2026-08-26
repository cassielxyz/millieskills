# React Native Reanimated 4

Use for React Native app motion when the project is compatible with Reanimated 4 / New Architecture.
Do not silently force a major architecture migration just to add animation.

## Preferred model
- shared values for animation state;
- worklets/UI runtime for frame-sensitive logic;
- `useAnimatedStyle`/props;
- Gesture Handler for direct manipulation;
- predefined entering/exiting/layout transitions before custom builders;
- scroll handlers for intentional scroll-linked state;
- system reduced-motion behavior.

## Performance
- avoid repeatedly reading shared values on the JS thread;
- prefer non-layout properties such as transform/opacity for frequent motion;
- avoid animating hundreds of React views simultaneously;
- memoize expensive gesture/frame callback definitions where appropriate;
- test release/debugOptimized behavior, not debug mode alone;
- inspect current RN/Reanimated feature-flag guidance when New Architecture regressions appear.

## Shared elements
Treat shared-element transitions as experimental when current Reanimated docs mark them so. Do not
make a critical navigation architecture depend on an experimental transition.

## Lists
For animated feeds/lists:
- stable keys;
- cap/offscreen virtualization;
- avoid every row running ambient animation;
- prefer list layout transitions over manual per-frame JS positioning.

## Reduced motion
Use system-aware configuration. Replace travel/scale/3D with fade/instant state when appropriate,
while preserving clear feedback.
