<div align="center">
  <img src="https://raw.githubusercontent.com/salvatorelaspata/awesome-sap/main/img/header.jpeg" alt="Awesome SAP">
</div>

# Awesome SAP ![Awesome](https://awesome.re/badge.svg)

A curated list of awesome documentation, tutorials, tools, tips, and community resources across the SAP ecosystem.

[SAP](https://www.sap.com) is a German multinational software corporation that provides enterprise software to manage business operations and customer relations.  
The SAP ecosystem spans multiple products and platforms, including SAP S/4HANA, SAP BTP, SAP Fiori/UI5, SAP NetWeaver, integration technologies, and more.

This list collects useful links for developers, consultants, architects, and anyone working with SAP: official documentation, community content, tools, samples, tutorials, and best practices.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

# Table of Contents

- [Global SAP Resources](#global-sap-resources)
- [SAP ABAP](#sap-abap)
- [SAP Fiori & UI5](#sap-fiori--ui5)
- [SAP S/4HANA](#sap-s4hana)
- [SAP BTP](#sap-btp)
- [SAP CPI / Integration](#sap-cpi--integration)
- [SAP Connectors](#sap-connectors)
- [License](#license)

---

## Global SAP Resources

General documentation, learning, and community entry points for the SAP ecosystem.

- [SAP Developer Center](https://developers.sap.com/) – Official entry point for tutorials, mission-based learning paths, and sample projects.
- [SAP Help Portal](https://help.sap.com/viewer/index) – Official product documentation and guides for SAP solutions.
- [SAP Community](https://community.sap.com/) – Q&A, blogs, events, and tags for all SAP topics.
- [SAP Learning](https://learning.sap.com/) – Free digital learning journeys and role-based training.
- [SAP Microlearning](https://microlearning.opensap.com/) – Short video learning content from SAP.
- [SAP TechEd](https://www.sap.com/events/teched.html) – Official annual SAP tech conference (sessions, replays, hands-on materials).
- [SAP Samples on GitHub](https://github.com/SAP-samples) – Official SAP sample projects on GitHub.
- [SAP Business Accelerator Hub (API Business Hub)](https://api.sap.com/) – SAP and partner APIs, integration content, and events.
- [SAP Podcasts](https://podcast.opensap.info/) – Podcasts on SAP technologies and strategy.
- [SAP Learning Hub (paid)](https://www.sap.com/training-certification/learning-hub.html) – Subscription-based learning platform for in-depth training.

---

## SAP ABAP

**[`^ back to top ^`](#table-of-contents)**

### Tools

- [ABAP in Eclipse (ADT)](https://tools.hana.ondemand.com/#abap) – ABAP Development Tools for modern ABAP development in Eclipse.
- [abapGit](https://abapgit.org/) – Git client for ABAP to manage ABAP code in Git repositories.

### OData / SAP Gateway

- [Transport OData Services – System Aliases](https://community.sap.com/t5/technology-blogs-by-members/transport-odata-services-system-aliases/ba-p/13461447)
- [Invalidate Metadata Cache for OData Services](https://community.sap.com/t5/technology-blogs-by-members/invalidate-metadata-cache-for-odata-services/ba-p/13446100)
- [Cache Cleanup in SAP NetWeaver Gateway](https://community.sap.com/t5/technology-blogs-by-members/cache-cleanup-in-sap-netweaver-gateway/ba-p/13362971)

> More ABAP, RAP, CDS, and Gateway resources welcome via pull requests.

---

## SAP Fiori & UI5

**[`^ back to top ^`](#table-of-contents)**

### Roadmap & Design

- [SAP Fiori Roadmap (interactive storyboard)](https://storyboard.cfapps.eu10.hana.ondemand.com/#/story/23ec6f30-26b1-483b-9171-a53bd85bb2e2) – Interactive SAP Fiori roadmap.
- [SAP Fiori Design Guidelines – Web](https://experience.sap.com/fiori-design-web/) – Official Fiori design guidelines for web applications.

### Fiori / UI5 Development Tools

- [UI5 Tooling](https://sap.github.io/ui5-tooling/) – CLI and libraries to develop, build, and deploy SAPUI5/OpenUI5 applications. ([GitHub](https://github.com/SAP/ui5-tooling))
- [SAP Business Application Studio (BAS)](https://pages.community.sap.com/topics/business-application-studio) – Cloud-based development environment for SAP Fiori and SAP BTP applications.
- [SAP Fiori Tools](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/2d8b1cb11f6541e5ab16f05461c64201.html) – Extensions for VS Code and SAP Business Application Studio to accelerate Fiori app development.
- [SAP Web IDE Personal Edition](https://help.sap.com/docs/help/825270ffffe74d9f988a0f0066ad59f0/5b8bca3147ee4dfd99be8aaf6bd4f421.html) – Legacy local edition of SAP Web IDE.

  > SAP Web IDE is deprecated on SAP BTP; consider SAP Business Application Studio and SAP Fiori tools instead.

- [Fiori Development with VS Code and Node.js](https://community.sap.com/t5/technology-blogs-by-members/fiori-development-with-vscode-and-nodejs/ba-p/13559117) – Step-by-step guide to Fiori development with VS Code and Node.js.

### SAPUI5 Freestyle

- [SAPUI5 SDK](https://sapui5.hana.ondemand.com/) – Documentation, API reference, samples, and demo apps for SAPUI5.
- [SAPUI5 SDK Download](https://tools.hana.ondemand.com/#sapui5) – SAPUI5 SDK tools page.

### SAP Fiori Elements

- [Overview of SAP Fiori Elements](https://experience.sap.com/fiori-design-web/smart-templates/) – Overview of template-based Fiori elements apps built on OData.

### SAP UI5 Web Components

- [UI5 Web Components – Official Documentation](https://sap.github.io/ui5-webcomponents/) – Web components for enterprise-grade UI based on SAP Fiori.

### Fiori Launchpad

- [Deploy SAPUI5 Applications on Fiori Launchpad](https://community.sap.com/t5/technology-blogs-by-members/deploy-sapui5-application-into-sap-fiori-launchpad/ba-p/13566643) – Step-by-step guide to deploy SAPUI5 apps to the Fiori Launchpad.

### Testing

- [OPA5](https://sap.github.io/ui5-tooling/pages/Opa5/) – JavaScript testing framework for UI5 integration tests.
- [WDI5](https://ui5-community.github.io/wdi5/#/) – UI5 testing framework with WebdriverIO integration.
- [Test Recorder](https://sapui5.hana.ondemand.com/sdk/#/topic/2535ef9272064cb6bd6b44e5402d531d) – Built-in SAPUI5 test recorder available in all supported browsers.
- [Playwright-Praman](https://praman.dev) – Playwright plugin for SAP UI5, Fiori, and S/4HANA test automation with AI test generation, typed control proxies, and OData V2/V4 support. ([GitHub](https://github.com/nicholasgma/playwright-praman), [npm](https://www.npmjs.com/package/playwright-praman))

---

## SAP S/4HANA

**[`^ back to top ^`](#table-of-contents)**

### SAP S/4HANA Cloud

_(Contributions welcome: official docs, extensibility, key user apps, in-app and side-by-side extension patterns.)_

### SAP S/4HANA On-Premise

_(Contributions welcome: installation and operations guides, simplification items, classic to S/4 migration, embedded analytics, etc.)_

---

## SAP BTP

**[`^ back to top ^`](#table-of-contents)**

### Programming Models & CAP

- [SAP Cloud Application Programming Model (CAP)](https://cap.cloud.sap/docs/) – Official CAP documentation (Node.js and Java).
- [Programming Models – SAP Help Portal](https://help.sap.com/docs/btp/sap-business-technology-platform/cloud-application-programming-model) – Help Portal entry for CAP and related programming models.

_(Contributions welcome: Kyma, Cloud Foundry, destinations, XSUAA, multitenancy, eventing, etc.)_

---

## SAP CPI / Integration

**[`^ back to top ^`](#table-of-contents)**

_(Contributions welcome: SAP Integration Suite, Cloud Integration (CPI), API Management, Open Connectors, patterns and best practices.)_

---

## SAP Connectors

**[`^ back to top ^`](#table-of-contents)**

Connectors for integrating SAP systems with different programming languages and runtimes.

- [ballerinax/sap](https://github.com/ballerina-platform/module-ballerinax-sap) – Official Ballerina connector for SAP S/4HANA.

_(Contributions welcome: .NET, Java, Node.js, Python, Go, and other community or official connectors.)_

---

## License

[![CC0](https://licensebuttons.net/l/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under a [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) License.
