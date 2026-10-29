## [3.0.0-dev.1](https://github.com/IMXEren/pydoll/compare/2.24.1...3.0.0-dev.1) (2026-10-29)

### ⚠ BREAKING CHANGES

* Upstream v3 replaces async properties with methods and removes deprecated 2.x APIs; the synchronous API is available under pydoll.sync.
* expect_cloudflare_turnstile is the only Turnstile handler
* name the Cloudflare helpers after what they do
* the async properties are now methods (tab.title(),
tab.current_url(), tab.page_source(), element.text(), element.inner_html(),
element.bounds(), element.iframe_context(), shadow_root.inner_html()), and
everything that raised DeprecationWarning in 2.x is removed: Tab.get_frame(),
the element argument of Tab.execute_script(), WebElement.key_down/key_up/
press_keyboard_key, type_text(interval=), Browser.start(headless=), the
custom_selector/time_before_click arguments of the Cloudflare helpers and the
NotAnIFrame/IFrameNotFound exceptions. _DownloadHandle is now DownloadHandle.

The top-level pydoll package exports the async API (Chrome, Edge, Tab,
WebElement, ShadowRoot, Keyboard, Mouse, Scroll, Request, Response,
DownloadHandle, ChromiumOptions, Key, ExtractionModel, Field, PageEvent,
NetworkEvent, FetchEvent) and pydoll.sync exports the same names, so the two
forms differ by one import line. The docs, README and examples use the new
imports and method calls, and a new "Upgrading to Pydoll 3" page lists every
change with its replacement.

### Features

* add browser fingerprint injection ([b85c3ae](https://github.com/IMXEren/pydoll/commit/b85c3ae859fa98881e7fc3b7591c7ddb81bd9d0b))
* enhance fingerprint application and management with new features and tests ([6d450e6](https://github.com/IMXEren/pydoll/commit/6d450e6083dcedc88a4c3b360a33ef2e1c30b5a2))
* **examples:** add a Linux desktop profile shaped for a container ([e832bc4](https://github.com/IMXEren/pydoll/commit/e832bc45d2ec7f46087d7f4052107f03296d8a63))
* **examples:** hide the globals that name the browser brand ([2ec2c6c](https://github.com/IMXEren/pydoll/commit/2ec2c6c0b8b215a7293e041ffcc2e671721a7b65))
* expect_cloudflare_turnstile is the only Turnstile handler ([bf7fa71](https://github.com/IMXEren/pydoll/commit/bf7fa7103f977ab3e3551bffc39637d09a90fb26))
* **fingerprint:** coherent headless screen via Emulation.updateScreen ([4400357](https://github.com/IMXEren/pydoll/commit/4400357a90c3467f96d0c0f9697f4caaccf61775))
* **fingerprint:** construct declared WebGL extensions and delegate without call/apply lookups ([9b9fa69](https://github.com/IMXEren/pydoll/commit/9b9fa699d79df78dcd79cc9dbf6b454cf9f0a069))
* **fingerprint:** cover the WebGL limits the hCaptcha payload actually asks for ([fa68691](https://github.com/IMXEren/pydoll/commit/fa686919e53ad2534c765887f7d0d54d32254626))
* **fingerprint:** emulate CSS media features via Emulation.setEmulatedMedia ([3aaeea0](https://github.com/IMXEren/pydoll/commit/3aaeea0a25344565f4b7245b8c1039a6d28105d3))
* **fingerprint:** hide the Web APIs the claimed OS does not implement ([7a37a53](https://github.com/IMXEren/pydoll/commit/7a37a532440906b044e04393396315fe8dd849d4))
* **fingerprint:** let the profile answer navigator.plugins and mimeTypes ([42cd23c](https://github.com/IMXEren/pydoll/commit/42cd23c892e34a8c54c699983d2f201e847ffe15))
* **fingerprint:** let the profile answer the media codec probes ([3195492](https://github.com/IMXEren/pydoll/commit/3195492b39b1f97f6e35e55647f82dbf237dc143))
* **fingerprint:** native-first overrides and Chromium client hints algorithm ([d519713](https://github.com/IMXEren/pydoll/commit/d5197137b08908cb8d0ff564a254d0a0d6c35dc5))
* **fingerprint:** propagate identity into cross-origin OOPIF iframes ([d7c91d9](https://github.com/IMXEren/pydoll/commit/d7c91d92508183eb54e5b2c4db4da76e61db34c1))
* **fingerprint:** rewrite browser-process script fetches with the profile identity ([cab3065](https://github.com/IMXEren/pydoll/commit/cab3065766cac898d4e6b7e6da77b468104316d7))
* **fingerprint:** WebGPU adapter profile ([6f6bd56](https://github.com/IMXEren/pydoll/commit/6f6bd567e83b9f38d353063b9fc0f638916e4612))
* **fingerprint:** WebGPU profiles for the Windows and Android examples ([c46dc1f](https://github.com/IMXEren/pydoll/commit/c46dc1f153edde3b0f7ece975b7c342eb2faaa48))
* humanized mouse inside iframes and shadow roots, moves sent without waiting ([8b0da38](https://github.com/IMXEren/pydoll/commit/8b0da38f2327eface6ba4b9076eb9b7f603ff3dc))
* implement fingerprint injection subsystem ([8caec00](https://github.com/IMXEren/pydoll/commit/8caec003423671432537e2e0a1711d2e4c6afb40))
* integrate upstream v3 with fork connection support ([e32b509](https://github.com/IMXEren/pydoll/commit/e32b509228bf99b8f2bdc238fa12a4dc8020b680))
* **playwright:** Playwright-compatible API layer (async and sync) over pydoll ([1d9b043](https://github.com/IMXEren/pydoll/commit/1d9b04341be94bc7ea4cf5e700968b9ad33cd353))
* **playwright:** run the layer on Pydoll 3 and test the documented flows ([c488da5](https://github.com/IMXEren/pydoll/commit/c488da55949a8899838b4fa542de79948e199515))
* pydoll 3, one API in sync and async form ([d31da53](https://github.com/IMXEren/pydoll/commit/d31da53e00097636bf6ec245c4437ee908c85933))
* say why the browser failed to start ([378ee39](https://github.com/IMXEren/pydoll/commit/378ee39b7e5151aa429a22b4ca3b6be95bf9f4df))
* **sync:** emit overloads, setters and every annotation dependency in the generated facades ([be908e5](https://github.com/IMXEren/pydoll/commit/be908e5f68c3486f1900848b28baaa3cac46d7f9))
* **sync:** generated synchronous API for pydoll ([2d86bc1](https://github.com/IMXEren/pydoll/commit/2d86bc1e92f9c68d28c6246706a55cf40cfb9e28))
* waits for element states, URLs, scripts, network idle, and expect_* capture blocks ([c27605d](https://github.com/IMXEren/pydoll/commit/c27605dd7d4a5bbfc7137a3f67ec7a5ee0b0ab60))

### Bug Fixes

* **browser:** close ConnectionHandler in OOPIF and iframe resolution ([14ff48a](https://github.com/IMXEren/pydoll/commit/14ff48aae803748bff14a54111bc03e8d61eb619))
* **browser:** guard empty tabs and None user_data_dir in Browser ([583a39f](https://github.com/IMXEren/pydoll/commit/583a39fc69d30504858695e1230aa49607f9dcff))
* **bundle:** rewrite root-relative URLs in HTML bundles ([7fabfbb](https://github.com/IMXEren/pydoll/commit/7fabfbba2eceb825f38b0c800e805a4e402aecca))
* change const to let for content and text variables ([d0b6930](https://github.com/IMXEren/pydoll/commit/d0b693047db31b452d09f59ae69edc1cca50b599))
* **ci:** restore mypy checks after uv migration ([0b5352f](https://github.com/IMXEren/pydoll/commit/0b5352ffc44ef7851a3bc98728b3fd45d67c6e0b))
* **cloudflare:** improve checkbox click logic for faster failure handling ([a6c89ec](https://github.com/IMXEren/pydoll/commit/a6c89ec6e7d5f6b4559dd4eb8a71cb0e4d61fc43))
* **cloudflare:** update checkbox selector and improve bypass logic ([305180a](https://github.com/IMXEren/pydoll/commit/305180a1b471d28f2129d8dbe049b6bd25c7828d))
* **decorators:** correct docstring example to use [@retry](https://github.com/retry) ([406c67c](https://github.com/IMXEren/pydoll/commit/406c67cc1e334d5ddc8323cb1327667ab6feceec))
* **examples:** complete the Android uniform families and enforce it ([7414753](https://github.com/IMXEren/pydoll/commit/7414753f7a9726d5169f880635edf80f9328c1b6))
* **examples:** declare WebGL on the Linux container profile ([aca787b](https://github.com/IMXEren/pydoll/commit/aca787bebf55be3d8c0045bbd04ba4628a7e1004))
* **examples:** drop the invalid webrtc_ip_policy from the container profile ([cf1febe](https://github.com/IMXEren/pydoll/commit/cf1febebedb746a3d19539d4cb4e5572a0448bfb))
* **examples:** use new_tab instead of removed get_page method ([b3a8e3e](https://github.com/IMXEren/pydoll/commit/b3a8e3e393fba67f2482b8bc67417384a23126de))
* **fingerprint:** anchor the example codec maps to measured answers ([d1ffb4e](https://github.com/IMXEren/pydoll/commit/d1ffb4e84e7edc94d133e5ebaab2bac50084fdf6))
* **fingerprint:** apply the WebGPU profile inside workers ([943014c](https://github.com/IMXEren/pydoll/commit/943014c92bc171446ce292f813eaf43dc1a82a62))
* **fingerprint:** check the font names a local() source asks for ([0b2f9e5](https://github.com/IMXEren/pydoll/commit/0b2f9e5bba2cc4b0ae9f331b2aac2d1be8bd0b1b))
* **fingerprint:** correct the transform-feedback enum mapping ([46eaa91](https://github.com/IMXEren/pydoll/commit/46eaa919dc7b2e363c9f09fcffd2b38313a3ccea))
* **fingerprint:** faithful constructor wrappers and non-cloneable fakes ([b18a1a5](https://github.com/IMXEren/pydoll/commit/b18a1a5ed4db5c055770489c189f27bd2f3016b0))
* **fingerprint:** give a patched method the native arity, not the callback's ([af53e1f](https://github.com/IMXEren/pydoll/commit/af53e1f817c66d1065a7a869c84997c7a5f1400c))
* **fingerprint:** keep Chrome's frozen Android platform and soften platformVersion claims ([caf3684](https://github.com/IMXEren/pydoll/commit/caf3684c63c27fe0e36d245e957c968bcb5c4c28))
* **fingerprint:** keep the emulation mode when a clamped window is reconciled ([17967b8](https://github.com/IMXEren/pydoll/commit/17967b843a9d84989afe6022380fcbc0aa4ae1b5))
* **fingerprint:** leave document.fonts.check() native ([020f891](https://github.com/IMXEren/pydoll/commit/020f891fdedee1d28e84c43b40a2e88a73e868c7))
* **fingerprint:** let touch emulation own navigator.maxTouchPoints ([03891d1](https://github.com/IMXEren/pydoll/commit/03891d11b7bcb5af6c4c54f98f8913498b74d7a6))
* **fingerprint:** make the values the profile reports physically possible ([840a07b](https://github.com/IMXEren/pydoll/commit/840a07b682c0e925957b60c81eacba456bf1d121))
* **fingerprint:** resolve script-fetch contexts by target and harden the JS residue ([c078eb3](https://github.com/IMXEren/pydoll/commit/c078eb398f1d6d8c1852dc10ec4018fb734c36cc))
* **fingerprint:** stop the override from rewriting Chrome's header order ([225953d](https://github.com/IMXEren/pydoll/commit/225953d7de169a27a15d5c2569dce80c42742b88))
* **fingerprint:** stop warning about the User-Agent the header path requires ([508362e](https://github.com/IMXEren/pydoll/commit/508362e1ee9b54cd4fe6f2cbba96c766eba9b163))
* **fingerprint:** treat an empty client_hints as no Client Hints at all ([f57b364](https://github.com/IMXEren/pydoll/commit/f57b36437f042aa5f82cee7d5c480414ad6e594d))
* harden the waiting API, the event worker and the WebGL override after review ([01e7c47](https://github.com/IMXEren/pydoll/commit/01e7c47825beeabbb241c6ff9bac4bddd906d095))
* **input:** read like real mouse and keyboard input, keep touch emulation after navigation ([8b536b9](https://github.com/IMXEren/pydoll/commit/8b536b9e4313d22c9baf46c95d1570a603c10ab4)), closes [#459](https://github.com/IMXEren/pydoll/issues/459)
* **js:** clear field on empty text in selection-read exception fallback ([2fbd5f7](https://github.com/IMXEren/pydoll/commit/2fbd5f7ef367e7b7ab2b4faf55bf5c237a7c1d00))
* **js:** guard selection restore for unsupported input types in INSERT_TEXT ([f7b1905](https://github.com/IMXEren/pydoll/commit/f7b19051ec3fd1cae6d6ea62f5e17bf69d9122b5))
* keep a margin when scrolling an element into view before clicking ([37eec7f](https://github.com/IMXEren/pydoll/commit/37eec7f4293aa0743fb33c1fa73a5182d1e75718))
* keep browser shutdown best effort on locked profile files, and tidy after review ([1e6b284](https://github.com/IMXEren/pydoll/commit/1e6b2843276ede5fd73a5953e278f71483a82086))
* keep worker and iframe session flows tolerant to rejected commands ([3ac6bdf](https://github.com/IMXEren/pydoll/commit/3ac6bdf5ae11d849fc1156cc79d0a51214f87bd1))
* narrow bare except in insert_text cache re-read ([2c74849](https://github.com/IMXEren/pydoll/commit/2c7484936cb8ffe907b8bdd2fbc3dacd063e61c2))
* nested iframes ([f3ec87c](https://github.com/IMXEren/pydoll/commit/f3ec87ce8b3aa205bac495e2834579fd5ac331f6))
* **playwright:** enter an expect block only after its event source is enabled ([28fa87c](https://github.com/IMXEren/pydoll/commit/28fa87cd765e56bea36d204e3402eca731c33d48))
* **playwright:** fractional clicks, geolocation accuracy, stale frames, wire headers and console handles ([deba286](https://github.com/IMXEren/pydoll/commit/deba2863112fc3bdb49c1867b535104e16ca86bb))
* **playwright:** make the context locale reach navigator.language ([5e59143](https://github.com/IMXEren/pydoll/commit/5e59143c71a395243340b418e423c17a9dcfe271))
* **playwright:** navigation, frames, lifecycle and error translation after review ([7588498](https://github.com/IMXEren/pydoll/commit/7588498d07f9f506e6bd72e158a6355928be8c2c))
* **playwright:** report an unreachable http DevTools endpoint as Error on every platform ([e77b9c3](https://github.com/IMXEren/pydoll/commit/e77b9c3cffe252c8dcd9be5babf2b8a36884e14d))
* **playwright:** resolve wait_until='commit' on frameNavigated so page.url is already set ([2a17f72](https://github.com/IMXEren/pydoll/commit/2a17f729bead226e6f867996719616b43792837d))
* preserve ws address when resolving iframe connections ([21ba225](https://github.com/IMXEren/pydoll/commit/21ba2251ec11ccf6cf97475add5932309f181c25))
* raise CommandFailed when the browser answers a command with an error ([b9b1094](https://github.com/IMXEren/pydoll/commit/b9b109448406969e9acb88c7dad9a78d01263007))
* replace deprecated asyncio.get_event_loop with get_running_loop ([ff08059](https://github.com/IMXEren/pydoll/commit/ff0805956c6ff96d3f6180bf367558aafc573e7d))
* resolve resource leaks and improve URL rewriting logic ([1c1983d](https://github.com/IMXEren/pydoll/commit/1c1983d277e839bcf774fd44b57c1609e41428a9))
* retry hook arity from its signature, and sync runtime fork, cancel and cache fixes ([8fc2a5b](https://github.com/IMXEren/pydoll/commit/8fc2a5bcd2dfbb38ab5244b5d7a64c3616735237))
* settle Runtime enabling before the next page command, and keep the instance for signature-less retry hooks ([80a496f](https://github.com/IMXEren/pydoll/commit/80a496f144057fd3f6a52c5d86b9f70d24d0ea02))
* **sync:** stop leaking a thread per callback and tighten the generated facade ([12e1f31](https://github.com/IMXEren/pydoll/commit/12e1f31b0a1abb50afc3a01676c0c1bc18e0f08c))
* **sync:** stop retaining facades, isolate callback threads, make the loop restartable ([59a44f4](https://github.com/IMXEren/pydoll/commit/59a44f4b3bfdd596594c53d2c104c317532d9edb))
* **test:** test_clear_input_in_iframe ([5614381](https://github.com/IMXEren/pydoll/commit/56143812d557ae6f45dcbe83ad6f640ec7206bca))
* **test:** test_find_element_in_parent_iframe ([c0ba97e](https://github.com/IMXEren/pydoll/commit/c0ba97eca8951253f923c8b0449196f9cc9425e3))
* update request to return raw data instead of encoded text ([83eaf22](https://github.com/IMXEren/pydoll/commit/83eaf22da76237154da635cb4bd4b4e28e545494))
* **utils:** use PATHEXT for executable validation on Windows ([c8a485e](https://github.com/IMXEren/pydoll/commit/c8a485e165192b75ee958e9c332c200d710f231b))

### Performance

* faster stop, quicker readiness poll, and log calls that cost nothing when off ([8e771ae](https://github.com/IMXEren/pydoll/commit/8e771ae56e8bf5aa3e177c027e85d1f93b19c4c7))
* send a typed string's key events as one batch ([238683d](https://github.com/IMXEren/pydoll/commit/238683d53ef8fab7f1e3be5bb85549d3e0b953db))
* stop sleeping where the browser has already answered ([eb69d80](https://github.com/IMXEren/pydoll/commit/eb69d8078658741a58970875518db00cc85eb54e))

### Documentation

* add Chinese documentation for migration, captcha bypass, evasion techniques, and human-like interactions ([17d7087](https://github.com/IMXEren/pydoll/commit/17d708700570145c8d2e467059fb07298f4ad54b))
* add fingerprint injection documentation and update navigation structure in mkdocs.yml ([68da0f7](https://github.com/IMXEren/pydoll/commit/68da0f79a54f66e302b8ea8158d4f2bbd4d00b7d))
* add height attributes to image tags in README ([675784a](https://github.com/IMXEren/pydoll/commit/675784acd1a4a380aa1e49a1ad36e536849c5a6f))
* add ipcook as top sponsor ([98772e0](https://github.com/IMXEren/pydoll/commit/98772e09570b718f09b1e0c23820af820cb361b2))
* add NodeMaven logo to README and update sponsorship section ([9f5dd20](https://github.com/IMXEren/pydoll/commit/9f5dd20eae27435abfba7c48cd6968e71ea37814))
* add NodeMaven sponsorship details to SPONSORS.md ([846d748](https://github.com/IMXEren/pydoll/commit/846d748e5851b202db086a53734e1a01b62c14b6))
* add swiftproxy logo image ([07386bc](https://github.com/IMXEren/pydoll/commit/07386bc23c824d10385e2be5be132ac05e5b5d96))
* announce Pydoll 3 at the top of the README and point feedback to issue [#463](https://github.com/IMXEren/pydoll/issues/463) ([692101c](https://github.com/IMXEren/pydoll/commit/692101c7098a13b4b66d3715160bb6d9715cb5a5))
* cut the template prose and the bold that read like a generator wrote them ([9489e06](https://github.com/IMXEren/pydoll/commit/9489e06b1b85cc4ddac93f7789fe7cee49c7732f))
* **deep-dive:** GPU, containers and what a profile cannot reach ([5ed96a7](https://github.com/IMXEren/pydoll/commit/5ed96a7bfa5fc745d1ddcf20cacf215cbafc3d89))
* enhance documentation clarity and structure across multiple files ([9b449dc](https://github.com/IMXEren/pydoll/commit/9b449dcd0d2c81278795e99f9a40a052fa9d26f5))
* enhance documentation with visual aids and interactive elements ([4dec8c5](https://github.com/IMXEren/pydoll/commit/4dec8c54e328079a989443394d4687b36b917f04))
* enhance sponsor section with improved layout and new sponsor details ([a8a075f](https://github.com/IMXEren/pydoll/commit/a8a075fda09f8b2cbde4b0be26029b925e30ddf1))
* escape iframe tag in API reference ([86782cd](https://github.com/IMXEren/pydoll/commit/86782cdb0777f71afe8406b0f9e5412fcc6a057d))
* **examples:** drop the explanatory comments from the profile module ([e2a45f7](https://github.com/IMXEren/pydoll/commit/e2a45f738c701c63f24ccdb3bea20fbaa7ee00c8))
* explain why the User-Agent major must equal the binary, and say what the override reaches ([dd5993d](https://github.com/IMXEren/pydoll/commit/dd5993d02d7a6a10c5b936cdc834ba36b73a86b5))
* **fingerprint-injection:** rewrite as a lean use guide (en/pt/zh) ([413fefa](https://github.com/IMXEren/pydoll/commit/413fefa6a69e9d956ce18e64de952f4d5d8574a3))
* **fingerprint-injection:** update descriptions for clarity in English, Portuguese, and Chinese versions ([bbc404a](https://github.com/IMXEren/pydoll/commit/bbc404a95b93065092e171573849b89d4b52bb51))
* **fingerprint:** add advanced fingerprinting deep dive ([337e95f](https://github.com/IMXEren/pydoll/commit/337e95f16474ef4c44914e04ff20894744800e8f))
* **fingerprint:** apply review corrections to the advanced fingerprinting deep dive ([4af0a18](https://github.com/IMXEren/pydoll/commit/4af0a18232d3a74f58922709780df89b34a85bef))
* **fingerprint:** cross-origin iframe coverage, Cloudflare deep dive, en/pt/zh ([5179380](https://github.com/IMXEren/pydoll/commit/5179380f7cde2ad2d8ed2a45f280c8239d0128a6))
* **fingerprint:** cut the narration from the profile comments ([6c7db51](https://github.com/IMXEren/pydoll/commit/6c7db5146c193e7fefe67573861846ff1682449c))
* fix the examples a review of the branch caught ([c218004](https://github.com/IMXEren/pydoll/commit/c21800454823c3f86d0523fbfd47de6a097991c8))
* give Playwright users a way in without making Pydoll a wrapper ([f9266d9](https://github.com/IMXEren/pydoll/commit/f9266d94ac3a5f44612f02840754ff14bbc0c080))
* make every Sync tab import pydoll.sync and fix the examples review caught ([c9590c4](https://github.com/IMXEren/pydoll/commit/c9590c4c222369a8003e5b6f506cb8606c46164e))
* **pt, zh:** mirror the containers section ([2234f6d](https://github.com/IMXEren/pydoll/commit/2234f6dd0c12718c793b59ee09c1cc498c69b5b7))
* **pt, zh:** mirror the fingerprint injection, spoofing limits and realms updates ([e1ccf27](https://github.com/IMXEren/pydoll/commit/e1ccf2724a4e39dcf5c044a355dcafe69ab41c24))
* **readme:** regenerate the Cloudflare gif as a live Turnstile bypass on the NopeCHA demo, in English ([9383a24](https://github.com/IMXEren/pydoll/commit/9383a2419dc47ae399a7668b65e05527be62cbcb))
* **readme:** rename Cloudflare gif to bust GitHub's image cache and point README at the new asset ([e010f53](https://github.com/IMXEren/pydoll/commit/e010f5312503aa2942928e792a784f3ea57c2af9))
* **readme:** sponsors first, then one quick start in both forms and the Playwright door ([a4a57b4](https://github.com/IMXEren/pydoll/commit/a4a57b45b5c96179cb2b253829d25160ad67cb77))
* rebuild embedded visuals as interactive animated simulations ([39a67b3](https://github.com/IMXEren/pydoll/commit/39a67b3fd722198a20cbb1f44db04b1ecd9a900f))
* refactor fingerprint injection documentation for clarity and consistency ([79259ec](https://github.com/IMXEren/pydoll/commit/79259ec8f71d18d5c3576bf39bd09dfeff94982a))
* refine language and improve clarity across multiple documentation files ([ceb7a57](https://github.com/IMXEren/pydoll/commit/ceb7a5752887a6bee9869c2d569bb791460944e3))
* remove AreYouHeadless from detection table ([7ec9211](https://github.com/IMXEren/pydoll/commit/7ec921166d884f884f6ae0d52ae8fc8ea9fce268))
* restructure sponsorship section with new layout and additional sponsor details ([7353711](https://github.com/IMXEren/pydoll/commit/73537114b23c0d32a61161fe1b69cb8a8bbf87b8))
* show every example as Sync and Async tabs ([0e9f5a6](https://github.com/IMXEren/pydoll/commit/0e9f5a66b62b5eb36c9ec5c71e154ac53b2ed845))
* **sponsors:** add SerpApi as the top sponsor ([f031d09](https://github.com/IMXEren/pydoll/commit/f031d0962557614210398fbf9368ae8d309318bc)), closes [#4668ea](https://github.com/IMXEren/pydoll/issues/4668ea)
* start the browser before creating a context in the per-context fingerprint example ([838d770](https://github.com/IMXEren/pydoll/commit/838d770b09f716caf0ed04a35b0aa091b0c42258))
* **stealth:** containers and servers without a GPU ([50f9edf](https://github.com/IMXEren/pydoll/commit/50f9edffcd966dbcd8dbf82756e810f68d1a5e2c))
* **stealth:** document headless screen coherence + avail_top/avail_left ([1a282aa](https://github.com/IMXEren/pydoll/commit/1a282aa87d5e312da0a0106bc0bd1eb27ca53bbc))
* **stealth:** keep the fingerprint pages at feature level ([4e78cbe](https://github.com/IMXEren/pydoll/commit/4e78cbe2882d17f2cba0520bc0c1f084bb48ccce))
* update documentation theme, landing page and README ([21b3c5f](https://github.com/IMXEren/pydoll/commit/21b3c5f687e416da4c62e457237c76fb92bdd658))
* update Google search demo image with a humanized interaction GIF ([656fa4b](https://github.com/IMXEren/pydoll/commit/656fa4b164df5a007b9321a076a7dc3f02da3bef))
* update image paths for fingerprint injection documentation ([06c2dcb](https://github.com/IMXEren/pydoll/commit/06c2dcb3b5d27a57fe4a2fd9c8c1fd49bc683de3))
* update maintainer note and sponsorship information in README ([62dcfd1](https://github.com/IMXEren/pydoll/commit/62dcfd1ee9c98f0cab9f73bd35f71314fd648dad))
* update NodeMaven logo dimensions and styles for improved visibility ([d46d438](https://github.com/IMXEren/pydoll/commit/d46d438b769bf6ab341fefe46e33e1c25fdf5d1f))
* update README ([bff441a](https://github.com/IMXEren/pydoll/commit/bff441a0c401a5220e77bcbafb944d84c0a342c8))
* update README ([69cff6b](https://github.com/IMXEren/pydoll/commit/69cff6bc5281f1e302400c4c8261f23163027277))
* update README by modifying badges and images ([1dc455d](https://github.com/IMXEren/pydoll/commit/1dc455dff858ee3d5441714ae085f178f1c32ae0))
* update README to enhance clarity on Pydoll's features and usage ([8b70209](https://github.com/IMXEren/pydoll/commit/8b70209422e45bdc77d8bb8c99d0884b9f383aba))
* update README with Nodemaven Proxy information ([f3f0a4b](https://github.com/IMXEren/pydoll/commit/f3f0a4b016fa04df9317d02764fc53a83d5ebbfa))
* update sponsor details and add CoreClaw and Proxy-Seller information ([1615a2a](https://github.com/IMXEren/pydoll/commit/1615a2a2381011934105853806ee6ab80687f89d))
* update sponsorship details and logos ([87cad21](https://github.com/IMXEren/pydoll/commit/87cad21afaebbdf695f827bb2d05e2fd5659ae7f))
* update sponsorship section with new layout, additional sponsors, and improved styling ([226d982](https://github.com/IMXEren/pydoll/commit/226d9821c835a9acf3e2f412191b7a4f96e0b6fb))
* update sponsorship section with NodeMaven and NiuProxy details, and replace banner images ([7d5e977](https://github.com/IMXEren/pydoll/commit/7d5e9774751d1b2df6f9e373445f2f8759a19834))
* **visuals:** contexts-isolation runs once and holds (no auto-loop) ([0983b52](https://github.com/IMXEren/pydoll/commit/0983b52baf1476651c632dd3657b5c8fb431db06))
* **visuals:** events-flow callback labels stack in-box (fix overflow) ([f4fa4d6](https://github.com/IMXEren/pydoll/commit/f4fa4d625d7c2d2bbd083ea7d9c1223ca8c8c025))

### Refactoring

* drop narration comments, section banners and the lint suppressions that hid real findings ([fc8b98e](https://github.com/IMXEren/pydoll/commit/fc8b98ec30a8fe7a5ebe3b6d93a16e1e17b7e8ff))
* **iframe:** extract _try_resolve_oopif to narrow try block ([76ba85c](https://github.com/IMXEren/pydoll/commit/76ba85c5d3a1e83d30907bcf742ece18b13a2124))
* make find_or_wait_element private ([1a2fc54](https://github.com/IMXEren/pydoll/commit/1a2fc548180b491095739ae47ce76a4b62a11b8f))
* name the Cloudflare helpers after what they do ([601f886](https://github.com/IMXEren/pydoll/commit/601f886833fef14633bd0625840a6b32ba46edee))
* **playwright:** fix the findings the removed suppressions exposed ([ea0bd6a](https://github.com/IMXEren/pydoll/commit/ea0bd6ac2e899598307a90441ad7ac0c9b763bee))
* remove outdated comments on fingerprint context handling ([4c64069](https://github.com/IMXEren/pydoll/commit/4c64069c20859f8b69a4a938c24fb241ba3cc129))
* spell unions with the | operator instead of typing.Union and Optional ([803dbc2](https://github.com/IMXEren/pydoll/commit/803dbc21d84943c74e34195fce0cecc7448b0f76))

### CI/CD

* fix GitHub Pages deployment ([96f629d](https://github.com/IMXEren/pydoll/commit/96f629d76279cbb69a54b6cef8ae4adb42168058))

### Chores

* drop narration comments from the input and worker fixes ([e42f7b6](https://github.com/IMXEren/pydoll/commit/e42f7b61fa4a044a69f29c959f64a1d495072fec))
* leave the changelog and the version to commitizen ([40fa742](https://github.com/IMXEren/pydoll/commit/40fa742f969876fc417daaed71a5ef02ff49f557))
* **sync:** regenerate the facades after merging main ([c6401b7](https://github.com/IMXEren/pydoll/commit/c6401b7a1c3c726e07c61d943483b2a8d54dbeff))
* **sync:** type-check the generated facades in CI ([0deea7d](https://github.com/IMXEren/pydoll/commit/0deea7df033530db80a10231f2b6b413f4712c19))

### Tests

* **playwright:** set the 150 ms default timeout after the navigation it is not meant to bound ([13795e0](https://github.com/IMXEren/pydoll/commit/13795e05bec3ad7159566f334e646d346063a9d6))
* regenerate the Playwright sync facade and give test launches a 60 s start timeout ([0b55306](https://github.com/IMXEren/pydoll/commit/0b55306e495ebf0f58335e3f6e88f6ff26219e6c))
* remove xfail markers and update mocks for fixed bugs ([d98a846](https://github.com/IMXEren/pydoll/commit/d98a846ecfc87312b0ed4e48498af65f50619c48)), closes [#5](https://github.com/IMXEren/pydoll/issues/5) [#6](https://github.com/IMXEren/pydoll/issues/6)
* share one browser per worker and run the suite in parallel ([51ce93f](https://github.com/IMXEren/pydoll/commit/51ce93f3368cdef5a436602ca7448941ec072638))

## [2.24.1](https://github.com/IMXEren/pydoll/compare/2.24.0...2.24.1) (2026-07-14)

### Bug Fixes

* **cloudflare:** re-query iframe body on each poll to avoid stale object_id ([456d86e](https://github.com/IMXEren/pydoll/commit/456d86e560e10d98b6d772519c15713dc897cacf))
* **connection:** import Required from typing_extensions for Python 3.10 compat ([609f2f8](https://github.com/IMXEren/pydoll/commit/609f2f8940faf3d95ae1f5fce16e5009a77e7e10))
* handle locked Session Storage files during Windows cleanup ([edcaab5](https://github.com/IMXEren/pydoll/commit/edcaab505bca903adf114acf4f13ecc9ea4faf08))
* resource leaks, incorrect behavior, and deprecation warnings ([29bde4e](https://github.com/IMXEren/pydoll/commit/29bde4e4bbafd0d1a678d26492282d830491f1bc))

### Documentation

* export WSAddressResolverParams and add field-level docstrings ([d388a0c](https://github.com/IMXEren/pydoll/commit/d388a0c8291ee13b13ce1cb1021f962f79867cff))

### CI/CD

* automate release pipeline with semantic-release ([e35f4fc](https://github.com/IMXEren/pydoll/commit/e35f4fc34e67198fb261bc3aca469bd651550118))
* remove build_pull_request.yml ([4c7aa42](https://github.com/IMXEren/pydoll/commit/4c7aa4260af5ec31b8141af1c5a8f2c63aaa142a))
* restrict push triggers to main to avoid PR overlap ([f99dc1c](https://github.com/IMXEren/pydoll/commit/f99dc1ced8f1873fe125ecca30b70b1070712087))
* **tests:** fix codecov file input ([ff31fc7](https://github.com/IMXEren/pydoll/commit/ff31fc7322a12b12b6ba1bbb1c3c4364abe499bd))

### Chores

* migrate repo references from autoscrape-labs to IMXEren ([3eb633d](https://github.com/IMXEren/pydoll/commit/3eb633d41021cb24a9792f63d5a375dee8ebc96e))
* release v2.24.1-dev.1 [skip ci] ([0715a3d](https://github.com/IMXEren/pydoll/commit/0715a3de5332cbf44019a299423f2391cf1b678c))
* release v2.24.1-dev.2 [skip ci] ([7d44fcc](https://github.com/IMXEren/pydoll/commit/7d44fccc20ae8359d9811a59a0dbb1473254a740))
* release v2.24.1-dev.3 [skip ci] ([516a7f5](https://github.com/IMXEren/pydoll/commit/516a7f5f57708b5a403af15b7c2cb1006f6e1efc))

### Tests

* relax humanized move assertion for fast timing on Windows ([b2cb5ba](https://github.com/IMXEren/pydoll/commit/b2cb5ba4e3761dd6bff490cd0efdaf2c9232985b))

## [2.24.1-dev.3](https://github.com/IMXEren/pydoll/compare/2.24.1-dev.2...2.24.1-dev.3) (2026-07-14)

### Bug Fixes

* handle locked Session Storage files during Windows cleanup ([edcaab5](https://github.com/IMXEren/pydoll/commit/edcaab505bca903adf114acf4f13ecc9ea4faf08))

### CI/CD

* remove build_pull_request.yml ([4c7aa42](https://github.com/IMXEren/pydoll/commit/4c7aa4260af5ec31b8141af1c5a8f2c63aaa142a))

## [2.24.1-dev.2](https://github.com/IMXEren/pydoll/compare/2.24.1-dev.1...2.24.1-dev.2) (2026-07-14)

### Bug Fixes

* resource leaks, incorrect behavior, and deprecation warnings ([29bde4e](https://github.com/IMXEren/pydoll/commit/29bde4e4bbafd0d1a678d26492282d830491f1bc))

## [2.24.1-dev.1](https://github.com/IMXEren/pydoll/compare/2.24.0...2.24.1-dev.1) (2026-07-14)

### Bug Fixes

* **cloudflare:** re-query iframe body on each poll to avoid stale object_id ([456d86e](https://github.com/IMXEren/pydoll/commit/456d86e560e10d98b6d772519c15713dc897cacf))
* **connection:** import Required from typing_extensions for Python 3.10 compat ([609f2f8](https://github.com/IMXEren/pydoll/commit/609f2f8940faf3d95ae1f5fce16e5009a77e7e10))

### Documentation

* export WSAddressResolverParams and add field-level docstrings ([d388a0c](https://github.com/IMXEren/pydoll/commit/d388a0c8291ee13b13ce1cb1021f962f79867cff))

### CI/CD

* automate release pipeline with semantic-release ([e35f4fc](https://github.com/IMXEren/pydoll/commit/e35f4fc34e67198fb261bc3aca469bd651550118))
* **tests:** fix codecov file input ([ff31fc7](https://github.com/IMXEren/pydoll/commit/ff31fc7322a12b12b6ba1bbb1c3c4364abe499bd))

### Chores

* migrate repo references from autoscrape-labs to IMXEren ([3eb633d](https://github.com/IMXEren/pydoll/commit/3eb633d41021cb24a9792f63d5a375dee8ebc96e))

## 2.24.0 (2026-07-11)

### Feat

- **connection**: add use_secure and WSAddressResolverParams TypedDict for resolver callbacks
- **connection**: support configurable connection_host for ConnectionHandler

### Fix

- **cloudflare**: update checkbox selector
- **connection**: add square brackets to host when ipv6 address
- **mouse**: keep debug overlay visible across page navigations

## 2.23.0 (2026-05-22)

### Feat

- enhance connection resilience and event handling in ConnectionHandler and managers
- implement User-Agent override propagation to worker contexts

### Fix

- avoid shared mutable default for WebElement attributes_list

### Refactor

- inject connection handler and managers for testability

## 2.22.1 (2026-04-10)

### Fix

- **requests**: surface JavaScript fetch errors with descriptive messages
- **requests**: surface JavaScript fetch errors with descriptive messages
- **requests**: surface JavaScript fetch errors with descriptive messages
- **requests**: surface JavaScript fetch errors with descriptive messages
- **test**: await canceled receiver task to avoid pending-task leaks
- add humanize to WebElement.click
- update broken webelement-domain link in element-finding.md
- update broken deep-dive links in core-concepts.md

## 2.22.0 (2026-03-23)

### Feat

- **extractor**: integrate extract and extract_all into Tab
- **extractor**: add module public API exports
- **extractor**: add extraction engine with CSS/XPath support
- **extractor**: add ExtractionModel base class
- **extractor**: add Field descriptor and ExtractionMetadata
- **extractor**: add extraction exception hierarchy
- add pydantic as required dependency
- add missing CDP enum values for AXPropertyName
- add missing enum values for AXPropertyName
- impl accesiblity domain

### Fix

- **test**: filter only DeprecationWarning in interval deprecated test
- **extractor**: correct coroutine type annotation for mypy
- **extractor**: resolve mypy type errors
- detect navigation errors on same-URL refresh in go_to
- use NavigateResponse type instead of dict with type ignore
- add type annotation to satisfy mypy var-annotated check
- add type annotation for navigate response
- raise NavigationError when go_to fails

### Refactor

- **extractor**: parallelize list field extraction with asyncio.gather
- **extractor**: use asyncio.gather for concurrent field extraction

## 2.21.3 (2026-03-14)

### Fix

- **test**: improve OOPIF integration test reliability
- **iframe**: resolve nested OOPIF iframes inside shadow roots

## 2.21.2 (2026-03-12)

### Fix

- release commit

## 2.21.1 (2026-03-03)

### Fix

- **keyboard**: send correct key, code and keycode in type_text
- **elements**: fix humanized interactions inside iframes
- humanized scroll overshoot correction causes infinite loop

## 2.21.0 (2026-03-01)

### Feat

- **interactions**: change humanize default from True to False

### Fix

- **elements**: forward humanize flag to click in type_text

## 2.20.2 (2026-02-18)

### Fix

- **command**: increase default command timeout from 10s to 60s across multiple components
- **tab**: remove temporary flag to avoid duplicate callback removal

## 2.20.1 (2026-02-16)

### Fix

- **tab**: replace readyState polling with CDP events in navigation

## 2.20.0 (2026-02-13)

### Feat

- **mouse**: add timing property for runtime configuration
- **requests**: add record() and replay() to Request class
- **requests**: add HAR network recorder
- **protocol**: add HAR 1.2 type definitions

### Fix

- **requests**: use surgical callback removal instead of nuclear clear_callbacks

### Refactor

- **tab**: extract bundle static methods to utils module

## 2.19.0 (2026-02-12)

### Feat

- **interactions**: default humanize=True for keyboard type_text
- **elements**: integrate Mouse API into WebElement.click()
- **interactions**: add Mouse API with humanized simulation
- **browser**: add webrtc_leak_protection property to ChromiumOptions
- **browser**: add automatic User-Agent consistency override

### Fix

- **utils**: harden SOCKS5 proxy forwarder security and robustness

## 2.18.0 (2026-02-11)

### Feat

- **utils**: add SOCKS5 proxy forwarder and convert utils to package
- **elements**: add cross-iframe selector support for XPath and CSS

## 2.17.0 (2026-02-08)

### Feat

- **tab**: refactor cloudflare bypass to use shadow root traversal
- **elements**: add shadow root timeout, CSS restriction and context propagation
- **tab**: add find_shadow_roots with OOPIF traversal and timeout
- **elements**: add shadow DOM support

### Fix

- **docs**: replace shadow.find() with query() in all documentation
- **tests**: replace shadow.find() with query() in integration tests
- **elements**: use float timeout and add contextual WaitElementTimeout messages

## 2.16.0 (2026-02-06)

### Feat

- add clear method for input and enhance page load state handling

### Fix

- **browser**: support secure websocket connections

## 2.15.1 (2026-01-04)

### Fix

- filter Symbol properties from element query results

## 2.15.0 (2025-12-24)

### Feat

- Implement incognito mode cookie retrieval for `tab.get_cookies()` and update related documentation

### Fix

- inconsistence in type checking
- Dispatch `KEY_DOWN` and `KEY_UP` events for character typing

## 2.14.0 (2025-12-10)

### Feat

- get_tab_by_target method added
- get_tab_by_target method added

### Fix

- adding type: ignore in JavascriptDialogOpeningEvent object
- adding type: ignore in JavascriptDialogOpeningEvent object

## 2.13.1 (2025-12-07)

### Fix

- add stuck scroll detection and minimum flick distance to humanized scroll, and correct scroll distance calculation.

## 2.13.0 (2025-12-07)

### Feat

- Implement humanized keyboard typing and physics-based scroll, and add iframe interaction support.

## 2.12.4 (2025-11-29)

### Fix

- optimize iframe resolution logic by adjusting backend node ID checks and enhancing child frame handling
- refine OOPIF resolution and frame attachment logic for improved handling of backend node IDs
- enhance OOPIF target attachment logic for improved session handling

## 2.12.3 (2025-11-27)

### Fix

- improve frame retrieval logic for better session handling

## 2.12.2 (2025-11-19)

### Fix

- adjust find_elements_mixin.py to refine return types and defaults

## 2.12.1 (2025-11-14)

### Fix

- continue cleanup process if temporary directory still exists
- adjust sleep duration for Windows and enhance temp dir cleanup
- enhance error handling for locked files on Windows systems
- remove unnecessary retry_times parameter in file processing
- ensure temp directory cleanup handles Chromium locked files
- enhance element selection and text extraction for better stability
- handle oopif targets
- change way to interact with iframes

### Refactor

- refactor iframe context handling in FindElementsMixin class

### Perf

- update Chrome options for better memory management and stability

## 2.12.0 (2025-11-04)

### Feat

- **execute_script**: validate element argument usage
- **tab,element,chrome**: revert arguments and add Chromium paths
- add a retry decorator for handling function execution failures

### Fix

- import TopLevelTargetRequired in test_browser_tab.py
- allow one additional retry attempt in the retry decorator

### Refactor

- **tab,element**: simplify execute_script parameters
- **element**: move and enhance execute_script from tab
- **tab**: separate execute_script concerns and enhance with comprehensive options

## 2.11.0 (2025-11-02)

### Feat

- add input handling functions and key constants for editing
- add KeyboardAPI for simulating keyboard input actions
- add KeyboardAPI integration for enhanced keyboard control

### Fix

- enhance text insertion and deprecate legacy key methods

## 2.10.0 (2025-11-01)

### Feat

- add ScrollAPI for enhanced page scrolling capabilities

## 2.9.3 (2025-10-30)

### Refactor

- keep take_screenshot consistent
- refactor type hints for better clarity and future compatibility

## 2.9.2 (2025-10-19)

### Fix

- update process creation to capture output and clean proxy format
- preserve query and fragment in WebSocket URL for tabs

### Refactor

- remove debug logging for request status and network events
- refactor logger messages to use consistent single quotes
- fix merge conflicts
- add logging for browser lifecycle and context management events
- refactor proxy parsing logic for improved clarity and efficiency

## 2.9.1 (2025-10-15)

### Fix

- change download event handling to use PageEvent instead of BrowserEvent

### Refactor

- use early return in setup proxy method

## 2.9.0 (2025-10-05)

### Feat

- add configurable page load state

## 2.8.2 (2025-10-03)

### Fix

- implement proxy authentication handling for browser tabs
- map exception when try to take screenshot of an iframe

## 2.8.1 (2025-09-27)

### Fix

- store the opened tab in the _tabs_opened dictionary
- **elements**: correctly detect parenthesized XPath expressions

### Refactor

- simplify FindElementsMixin._get_expression_type startswith checks into single tuple

## 2.8.0 (2025-08-28)

### Feat

- adding get_siblings_elements method
- adding get_children_elements method
- refactor Tab class to support optional WebSocket address handling
- add WebSocket connection support for existing browser instances
- add optional WebSocket address support in connection handler

### Fix

- add get siblings and get childen methods a raise_exc option
- improving children and parent retrive docstring and creating a private generic method for then
- using new execute_script public method
- solving conflicts
- rename pages fixtures files and adding a error test

### Refactor

- refactor Tab class to improve initialization and error handling
- refactor Browser class to manage opened tabs and WebSocket setup
- add new exception classes for connection and WebSocket errors

## 2.7.0 (2025-08-22)

### Feat

- refactor WebElement methods to use a unified naming convention
- add Response type and new bring_to_front method to Tab class
- improve element interactability scripts

### Fix

- **browser**: add google-chrome-stable path for Arch Linux AUR package
- run actions to fix badges
- enforce combined condition logic in wait_until
- **web_element**: raise WaitElementTimeout on wait_until timeout

### Refactor

- update command responses to use Response for empty responses
- **webelement**: simplify wait_until condition mapping

## 2.6.0 (2025-08-10)

### Feat

- add DownloadTimeout exception for file download timeouts
- add context manager for handling file downloads in Tab class

### Refactor

- add type checking for connection handler in mixin class
- add type overloads for event callback in Browser class

## 2.5.0 (2025-08-07)

### Feat

- add HTTP client functionality using the browser's fetch API
- add HTTP response object for browser-based fetch requests
- implement Request class for HTTP requests using fetch API
- add Request handling and improve network log retrieval methods

### Fix

- reject cookies with empty names during parsing in Request class
- refactor imports to include NotRequired and TypedDict from typing_extensions
- update imports to use typing_extensions for compatibility reasons
- check for None in events_enabled before updating params
- remove unused event type aliases and clean up imports

### Refactor

- depreciating headless argument in start method and adding it in to browser options properties
- add asynchronous function for makeRequest in JavaScript
- refactor imports for cleaner organization and improved clarity
- refactor type hints in FindElementsMixin for clarity and type safety
- refactor type hints and improve command method signatures
- refactor event handling to use specific event types for clarity
- refactor connection handler to use CDPEvent and typed commands
- refactor storage command methods to return specific command types
- refactor target command methods to use specific command types
- refactor command return types to specific command classes
- refactor page commands to use specific command types directly
- refactor network commands to use specific command types
- refactor input command methods to return specific command types
- refactor fetch_commands to use updated type definitions
- refactor enums to inherit from str for better compatibility
- refactor DOM command types for improved code clarity and structure
- refactor command and event parameter types for better typing
- refactor command responses to use EmptyResponse where applicable
- improve protocol types for target domain
- improve protocol types for storage domain
- refactor command response types for improved readability and consistency
- improve protocol types for page domain
- add IncludeWhitespace and RelationType enums to DOM types
- improve protocol types for input domain
- refactor AuthChallengeResponse and remove legacy definitions
- remove legacy WindowBoundsDict for cleaner type definitions
- add new TypedDicts and enums for runtime event parameters
- refactor DOM event types and methods for better clarity and structure
- refactor fetch command return types for better clarity and structure
- enhance browser command functionality with new methods and types
- add TypedDict and Enum definitions for emulation and debugging
- improve protocol types for network domain

## 2.4.0 (2025-08-01)

### Feat

- changing bool prefs to properties and adding support to user-data-dir preferences
- adding prefs options customization
- add overloads for find and query methods in FindElementsMixin
- add method to retrieve parent element and its attributes
- implements start_timeout option

### Fix

- adding typehint and fixing some codes
- removing options preferences private attributes
- set default URL to 'about:blank' in create_target method
- change navigation when creating a new tab
- add type hinting support and update project description

### Refactor

- remove redundant asterisk from find method overloads and reorganize query method overloads
- refine type hint for response parameter and improve key check

## 2.3.1 (2025-07-12)

### Fix

- refactor click_option_tag to use direct script reference
- update script to use closest for more reliable DOM selection
- improve selection script for higher accuracy
- use correct class name and id selector in query()
- add fetch command methods to handle request processing

### Refactor

- change body type from dict to string in fetch command parameters
- refactor continue_request and fulfill_request to use options
- enhance continue_request and fulfill_request with new options

## 2.3.0 (2025-06-25)

### Feat

- **connection**: Upgrade adapt websockets version to 14.0

### Fix

- refine selector condition to include attributes check

## 2.2.3 (2025-06-20)

### Fix

- fix contextmanager for file upload

## 2.2.2 (2025-06-18)

### Fix

- fix call_function_on parameters order

### Refactor

- replace BeautifulSoup with custom HTML text extractor

## 2.2.1 (2025-06-16)

### Fix

- fix call parameters order in call_function_on method

## 2.2.0 (2025-06-15)

### Feat

- add method to retrieve non-extension opened tabs as Tab instances

### Refactor

- refactor attribute assignments to include type annotations
- implement singleton pattern for Tab instances by target_id

## 2.1.0 (2025-06-14)

### Feat

- add new script-related exception classes for better handling
- add functions to clean scripts and check return statements
- add methods to retrieve network response body and logs

### Fix

- click in the input before typing and fix documentation

### Refactor

- add overloads for execute_script to improve type safety

## 2.0.1 (2025-06-08)

### Fix

- fix private proxy configuration

## 2.0.0 (2025-06-08)

### BREAKING CHANGE

- pydoll v2 finished

### Feat

- intuitive way to interact with iframes
- refactor Keys class to Key and add utility methods for enums
- add Event TypedDict for standardized event structure
- add TargetEvent enum for Chrome DevTools Protocol events
- add StorageEvent enumeration for Chrome DevTools Protocol events
- add RuntimeEvent enumeration for Chrome DevTools Protocol events
- add PageEvent enumeration for Chrome DevTools Protocol events
- add NetworkEvent enumeration for Chrome DevTools Protocol events
- add InputEvent enum for Chrome DevTools input events
- add FetchEvent enumeration for Chrome DevTools Protocol events
- add DomEvent enumeration for Chrome DevTools Protocol events
- add BrowserEvent enum for Chrome DevTools protocol events
- add methods to enable and disable the runtime domain commands
- add new enums for whitespace, axes, pseudo types, and modes
- add DOM response types and corresponding response classes
- add DOM command types and parameter definitions for pydoll
- add enums for key, mouse, touch, and drag event types
- add input command types for touch, mouse, and keyboard events
- enhance TargetCommands class with new methods for targets management
- add TypedDicts for target response types and browser contexts
- add TypedDict definitions for target command parameters
- add storage-related enumerations for bucket durability and types
- enhance StorageCommands with new methods for data management
- add storage response types and related classes for handling data
- add storage command types using TypedDict for structured params
- add new enumeration classes for serialization and object types
- add runtime response types for handling various object previews
- add initial runtime command types for protocol handling
- add constants for various encoding, formats, and policies
- add TypedDict definitions for page response types and results
- add typed dictionaries for various page command parameters
- add new command parameter classes for network resource handling
- add TypedDict definitions for network response types
- organize command types into structured imports and exports
- add network command types and parameters for cookie management
- add enums for cookie priorities, connection types, and encodings
- add response classes for browser window target retrieval
- setup mkdocs and install related packages
- add async text property for retrieving element text

### Fix

- remove target directory from .gitignore file
- fix typo in USB_UNRESTRICTED constant for consistency
- add new network command parameters and methods for cookies
- change postData type from dict to string in ContinueRequestParams

### Refactor

- refactor screenshot path handling and enhance error checking
- refactor type hints from List to built-in list for consistency
- refine XPath condition handling and ensure integer coordinates
- refactor condition checks to ensure against None values
- refactor exception handling and add browser path validation function
- rename BrowserOptionsManager to ChromiumOptionsManager
- refactor Edge class to use ChromiumOptionsManager and simplify path validation
- refactor Chrome class to use Chromium-specific options manager
- refactor Browser class to use options manager and improve methods
- refactor Options class to ChromiumOptions and use type hints
- refactor to create ChromiumOptionsManager for better clarity
- add abstract base classes for browser options management
- use `message.get('id')` for safer ID checks in response
- refactor message handling to support multiple message types
- refactor element finding methods for enhanced flexibility and clarity
- rename method for better clarity in captcha element handling
- refactor type hints for event callback parameters and options
- simplify ping call by inlining WebSocketClientProtocol cast
- refactor EventsManager to use typed Event objects consistently
- add runtime events management to the Tab class functionality
- update event callback signatures for better type handling
- remove unused import of Response in runtime_commands.py
- add Response import to page_commands for improved functionality
- refactor response classes to use TypedDict for better typing
- refactor WebElement class to organize exception imports clearly
- refactor exception handling in FindElementsMixin class
- refactor exception handling to use custom timeout and connection errors
- remove unused import statements in events_manager.py
- refactor error handling to use specific exceptions for clarity
- refactor error handling to use custom exception for arguments
- fix PermissionError raising in TempDirectoryManager class
- refactor error handling to use specific exceptions for clarity
- handle unsupported OS with a custom exception in Edge class
- raise UnsupportedOS exception for unsupported operating systems
- refactor browser error handling and improve method return types
- refactor exception classes to improve organization and clarity
- refactor element finding methods to use updated command structure
- refactor WebElement class for improved structure and clarity
- refactor import statements and clean up code formatting
- refactor command imports and enhance download behavior method
- refactor Tab import and update FetchCommands method calls
- refactor ConnectionHandler docstrings for clarity and conciseness
- refactor command and event managers for improved type safety
- refactor ConnectionHandler to improve WebSocket management and clarity
- add Tab class for managing browser tabs via CDP integration
- enhance TempDirectoryManager with detailed docstrings and type hints
- refactor ProxyManager to enhance proxy credential handling
- refactor Browser class to enhance automation capabilities and structure
- move commands to a different module
- define base structures for commands and responses in protocol
- import Rect from dom_commands_types for response handling
- refactor cookie-related types for improved clarity and consistency
- remove unnecessary whitespace in docstring of InputCommands class
- refactor DOM commands to improve structure and add functionality
- refactor InputCommands to enhance user input simulation methods
- add CookieParam TypedDict to define cookie attributes
- add new runtime command methods for JavaScript bindings and promises
- remove unused method to clear accepted encodings in network commands
- update ResetPermissionsParams to use NotRequired for context ID
- refactor PageCommands to improve structure and add type hints
- simplify import statements by using wildcard imports for responses
- add new response types and update existing response classes
- consolidate command imports using wildcard imports for clarity
- correct post_data type from dict to str in FetchCommands class
- refactor NetworkCommands to use structured command parameters
- refactor fetch command methods to use static methods directly
- refactor BrowserCommands to use static methods and improve clarity
- refactor response imports and update __all__ definitions
- refactor import statements for better readability and structure
- refactor import statements for consistency in response types
- refactor import and rename EnableParams to FetchEnableParams
- refactor import statement for CommandParams module path
- refactor fetch command templates to use Command class
- add enums for window states, download behaviors, and permissions
- remove unused enum imports and rename base_types module
- refactor command structures for better organization and clarity
- rename command and response modules for better clarity
- refactor imports for better organization and readability
- add browser command methods for version, permissions, and downloads
- add command and response types for protocol implementation
- refactor execute_command to use type annotations for clarity
- refactor command methods to specify response types in BrowserCommands
- refactor command structures and introduce base CommandParams class
- refactor browser command constants to use Command class type
- refactor connection imports and rename manager files for clarity
- refactor BrowserType import to a common constants module
- refactor browser modules to use the new chromium structure
- refactor element imports and remove deprecated element file
- refactor import paths to use the protocol submodule structure
- move command files to the protocol directory for better structure
- rename insert_text to paste_text and remove unused files
- refactor the `InputCommands` class to enhance clarity and simplicity in its operations
- add deprecation warning to get_element_text()

## 1.7.0 (2025-04-06)

### Feat

- refactor captcha handling with adjustable wait times and parameters

## 1.6.0 (2025-04-06)

### Feat

- add connect method to handle existing port scenarios
- create enable_auto_solve_cloudflare_captcha method
- add context manager to bypass Cloudflare Turnstile captcha

## 1.5.1 (2025-03-31)

### Fix

- handle headers input as list or dictionary in fetch command

## 1.5.0 (2025-03-26)

### Feat

- add flag to run browser on headless mode on start function

### Fix

- Wait for the file `CrashpadMetrics-active.pma` to be deoccupied and cleaned up
- Catch websockets.ConnectionClosed errors on duplicate close()
- move connection closed log inside if statement

## 1.4.0 (2025-03-23)

### Feat

- Update initialize_options method to allow optional browser_type parameter
- Refactor Edge browser options handling to use EdgeOptions class
- Supports initialization options based on browser type
- Edge browser constructors to support optional connection port parameters
- Add Microsoft Edge browser support
- 为 Edge 浏览器添加默认用户数据目录支持
- Add Microsoft Edge browser support

### Refactor

- Clean up imports and improve code formatting across browser modules
- Simplify user data directory setup and enhance Edge browser path handling

## 1.3.3 (2025-03-18)

### Fix

- solve browser invalid domain events issue
- improve process termination
- improve process management and deactivate websockets connection size limit

### Refactor

- import commands and evebts from __init__.py

## 1.3.2 (2025-03-13)

### Fix

- fixed the tests and used lint for the OS multi path support
- support multiple default Chrome paths on each OS

## 1.3.1 (2025-03-12)

### Fix

- remove unnecessary encoding from screenshot response data

## 1.3.0 (2025-03-12)

### Feat

- add method to retrieve screenshot as base64 encoded string

## 1.2.4 (2025-03-11)

### Fix

- refactor Chrome constructor to use Optional for parameters

## 1.2.3 (2025-03-11)

### Fix

- refactor proxy configuration retrieval for cleaner code flow

## 1.2.2 (2025-03-10)

### Fix

- Get file extension from file path and changes use of reserved word 'format' to 'fmt'

## 1.2.1 (2025-03-09)

### Fix

- resolve issue #29 where browser path was not found on macOS
- Quickstart code given in README is wrong

## 1.2.0 (2025-02-11)

### Feat

- add close method and command to Page class functionality

## 1.1.0 (2025-02-11)

### Feat

- add method to retrieve Page instance by its ID in Browser class

## 1.0.1 (2025-02-10)

### Fix

- add dialog property to ConnectionHandler and manage dialog state

## 1.0.0 (2025-02-05)

### BREAKING CHANGE

- now you'll have to use By.CSS_SELECTOR instead of By.CSS

### Feat

- refactor import and export statements for better readability
- update changelog for version 0.7.0 and fix dependency versions
- add ping method to ConnectionHandler for browser connectivity check
- add tests for BrowserCommands in test_browser_commands.py

### Fix

- add initial module files for commands, connection, events, and mixins
- add connection port parameter to Chrome browser initialization
- use deepcopy for templates to prevent mutation issues

### Refactor

- rename constant CSS to CSS_SELECTOR
- add command imports and remove obsolete connection handler code
- refactor methods to be static in ConnectionHandler class
- refactor proxy configuration and cleanup logic in Browser class
- refactor ConnectionHandler to improve WebSocket management logic
- refactor Browser class initialization for better clarity and structure
- refactor Browser initialization to enhance flexibility and defaults
- refactor import statement for ConnectionHandler module
- refactor import paths for ConnectionHandler in browser modules
- implement ConnectionHandler for WebSocket browser automation
- implement command and event management for asynchronous processing
- remove unnecessary logging for WebSocket address fetching
- refactor Chrome class to use BrowserOptionsManager for path validation
- implement proxy and browser management in the new managers module
- refactor Browser class to use manager classes for better structure
- refactor DOM command scripts for clarity and efficiency

## 0.7.0 (2024-12-09)

### Feat

- autoremove dialog from connection_handler when closed
- add handle_dialog method to PageCommands class
- add dialog handling methods to Page class
- add support for handling JavaScript dialog opening events
- refactor network response handling for base64 encoding support
- add clipping option for screenshots and implement element capture

### Fix

- index error on method get_dialog_message
- update screenshot format from 'jpg' to 'jpeg' for consistency
- handle potential IndexError when retrieving valid page targetId
- filter valid pages using URL condition instead of title check

### Refactor

- run ruff formatter to ensure code consistency
- run ruff formatter to ensure code consistency
- change screenshot format from PNG to JPG in commands and element

## 0.6.0 (2024-11-18)

### Feat

- add callback ID handling for page load events in Page class
- update event registration to return callback IDs and add removal
- refactor DOM commands to use object_id instead of node_id

### Fix

- refactor page navigation and loading logic for efficiency
- add page reload after navigating to a new URL in Page class
- refactor URL navigation to use evaluate_script for efficiency
- implement page refresh on URL unchanged and add navigation event
- update object ID reference in Page class for clarity
- refactor element search logic to simplify error handling
- DomCommands using `object_id` instead of `node_id` to prevent bugs
- handle OSError when cleaning up temporary directories in Browser

### Refactor

- change error log to warning for missing callback ID
- refactor DOM command scripts for improved readability and reuse
- rename methods for clarity and consistency in WebElement class
- refactor parameter names for consistency in target methods
- normalize variable naming for consistency in fetch commands

## 0.5.1 (2024-11-12)

### Fix

- simplify outer HTML retrieval for consistent object handling
- refactor click method to check option tag earlier in flow
- refactor bounding box retrieval to access nested response value
- handle KeyError instead of IndexError for element bounds retrieval
- enhance DOM command methods and rename for clarity and consistency
- add JavaScript bounding box retrieval for web elements
- remove redundant top-checks for element clicks in WebElement

## 0.5.0 (2024-11-11)

### Feat

- add method to generate command for calling a function on an object
- implement script execution and visibility checks in click method
- add JavaScript functions for element visibility and interaction

### Refactor

- enhance exception classes with descriptive error messages
- simplify command creation by using RuntimeCommands.evaluate_script
- refactor JavaScript execution and introduce runtime commands

## 0.4.4 (2024-11-11)

### Fix

- remove redundant DOM content loaded event handling logic

## 0.4.3 (2024-11-11)

### Fix

- rename event variables for clarity and improve timeout handling

### Refactor

- remove debug print statement from connection event handling

## 0.4.2 (2024-11-11)

### Fix

- update event handling to use DOM_CONTENT_LOADED for page load
- convert Browser context management to async methods

### Refactor

- fix string formatting in logger info message for clarity

## 0.4.1 (2024-11-08)

### Fix

- fixes workflow removing unnecessary hifen
- reduce sleep duration in key press handling for improved speed

## 0.4.0 (2024-11-08)

### Feat

- add type_keys method for realistic key input simulation

## 0.3.1 (2024-11-08)

### Fix

- addning new package version
- removing encode utf8 in get_pdf_base64

## 0.3.0 (2024-11-08)

### Feat

- set_download_path added in browser class methods

## 0.2.0 (2024-11-08)

### Feat

- dynamic lib version using pyproject

## 0.1.1 (2024-11-07)

### Fix

- ensure browser process terminates after executing close command

## 0.1.0 (2024-11-07)

### Feat

- add method to delete all cookies from the browser session
- add is_enabled property to check element's enabled status
- add option to raise exception in wait_element method
- add method to set browser download path via command
- refactor text extraction using BeautifulSoup for accuracy
- add method to get properties and improve XPath handling
- refactor text retrieval methods and improve code readability
- add timeout parameter to page navigation and loading methods
- add cookie management and scroll into view functionality
- add method to retrieve page PDF data as base64 string
- add async property to retrieve inner HTML of the element
- add async page_source property to retrieve page source code
- add async property to retrieve the current page URL
- add method to find multiple DOM elements using selectors
- refactor WebElement to use FindElementsMixin for clarity
- add FindElementsMixin for asynchronous DOM element handling
- add methods to retrieve network response bodies from logs
- add method to retrieve matching network logs from the page
- add cookie management methods to the Browser class
- add ElementNotFound exception to handle missing elements
- add value property and handle option tag clicks in WebElement
- rename FIND_ELEMENT_XPATH_TEMPLATE to EVALUATE_TEMPLATE
- add exception handling for element not found in find_element method
- downgrade Python version requirement to 3.10 in pyproject.toml
- add async function to fetch browser WebSocket address
- simplify text input handling by using insert_text command
- add TargetCommands class for managing target operations
- add method to generate command for disabling the Page domain
- add method to generate text insertion commands for inputs
- add Page class to manage browser page interactions and events
- add page management methods to the Browser class
- add detailed logging for command responses and event handling
- add event classes for browser, DOM, fetch, and network actions
- add NetworkCommands class for managing network operations
- implement fetch command methods for handling requests and responses
- add method to enable DOM domain events in DomCommands class
- add proxy configuration and fetch event handling to Browser
- refactor connection errors to use custom exceptions for clarity
- add methods to clear callbacks and close WebSocket connection
- remove unnecessary newline at the end of PageEvents class file
- add context managers and async file handling for efficiency
- implement singleton pattern and prevent multiple initializations
- add dynamic connection port handling for browser instance
- add temporary directory management for browser session storage
- add logging for connection events and command executions
- add PageEvents class with PAGE_LOADED event constant
- add temporary callback option to event registration method
- add page event handling and improve loading timeout management
- add utility function to decode base64 images to bytes
- add WebElement class for handling browser elements asynchronously
- add enumeration for selector types in constants module
- add PageCommands class for browser page control functions
- add InputCommands class for handling mouse and keyboard events
- implement DOM commands for interacting with web elements
- refactor BrowserCommands to include new window management methods
- implement some basic methods to navigate and control the browser instance
- enhance ConnectionHandler with detailed docstrings for methods
- add .gitignore, .python-version, and poetry.lock files

### Fix

- browser context now uses the storage commands to get cookies, while the page context us cookies, while page context uses network
- update cookie retrieval to use NetworkCommands for consistency
- remove download path method from Browser and add to Page class
- add options to disable first-run and browser check flags
- handle KeyError when retrieving network response bodies
- use get() to safely retrieve attributes in WebElement class
- rename class attribute retrieval for clarity and consistency
- enhance get_properties and simplify text retrieval method
- enhance create_web_element call with additional value parameter
- fix incorrect key access in JavaScript evaluation result
- update cookie management to clear browser cookies correctly
- filter pages by title instead of URL in Browser class
- filter out non-page entries when fetching valid page IDs
- xpath element solved
- refactor event callback storage to use unique callback IDs
- add JavaScript execution method and enhance click offsets
- simplify response handling and improve event callback structure
- reorder page event enabling to ensure proper browser startup
- add JSON handling and improve WebSocket command execution

### Refactor

- improve WebElement representation and handle None for nodeValue
- add newline at end of file for ElementNotFound exception class
- remove unused aiohttp import and clean up whitespace
- remove unnecessary blank lines in storage.py for clarity
- fix missing newline at the end of the file in page.py
- remove unnecessary whitespace in InputCommands class methods
- refactor DOM command methods for improved clarity and usability
- refactor Page class to inherit from FindElementsMixin
- refactor code to remove duplicate import of StorageCommands
- clarify error messages for command and callback validation
- refactor ConnectionHandler to simplify initialization and connect logic
- remove unnecessary whitespace in element.py for cleaner code
- refactor WebElement to enhance attribute retrieval methods
- refactor connection handling and improve error messaging
- refactor Browser class to use abstract base class and commands
