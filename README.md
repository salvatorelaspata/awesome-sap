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
- [Clean Core & Extensibility](#clean-core--extensibility)
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

### ABAP RESTful Application Programming Model (RAP)

- [ABAP RESTful Application Programming Model – Help Portal](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/289477a81eec4d4e84c0302fb6835035.html) – Official RAP documentation and developer guide.[web:31]
- [ABAP RESTful Application Programming Model – SAP Community Topic Page](https://pages.community.sap.com/topics/abap/rap) – Blogs, Q&A, and learning resources around RAP.[web:39]
- [ABAP Cloud & RAP Overview (PDF)](https://blog.asug.com/hubfs/Chapter%20Events/ABAP%20Cloud%20-%20RAP%20-%20S4HANA%20Extensibility.pdf) – Slide deck introducing ABAP Cloud and RAP, including extensibility and roadmap.[web:42]
- [ABAP Extensibility Guide – Clean Core for SAP S/4HANA Cloud](https://community.sap.com/t5/technology-blog-posts-by-sap/abap-extensibility-guide-clean-core-for-sap-s-4hana-cloud-august-2025/ba-p/14009741) – Official blog explaining ABAP Cloud-based extensibility and its evolution with clean core levels.[web:48]

> Contributions welcome: CDS views, RAP tutorials, clean core patterns, testability, and best practices.

---

## SAP Fiori & UI5

**[`^ back to top ^`](#table-of-contents)**

### Roadmap & Design

- [SAP Fiori Roadmap (interactive storyboard)](https://storyboard.cfapps.eu10.hana.ondemand.com/#/story/23ec6f30-26b1-483b-9171-a53bd85bb2e2) – Interactive SAP Fiori roadmap.
- [SAP Fiori Design Guidelines – Web](https://experience.sap.com/fiori-design-web/) – Official Fiori design guidelines for web applications.

### Fiori / UI5 Development Tools

- [UI5 Tooling](https://sap.github.io/ui5-tooling/) – CLI and libraries to develop, build, and deploy SAPUI5/OpenUI5 applications. ([GitHub](https://github.com/SAP/ui5-tooling))
- [SAP Business Application Studio (BAS)](https://pages.community.sap.com/topics/business-application-studio) – Cloud-based development environment for SAP Fiori and SAP BTP applications.
- [SAP Fiori Tools](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/2d8b1cb11f6541e5ab16f05461c64201.html) – Extensions for VS Code and SAP Business Application Studio to accelerate Fiori app development.[web:13]
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

## Clean Core & Extensibility

**[`^ back to top ^`](#table-of-contents)**

Resources focused on keeping the digital core clean while building upgrade-stable, cloud-compliant extensions using ABAP Cloud, RAP, CAP, and SAP BTP.

### Concepts & Whitepapers

- [Introducing the Clean Core Approach – SAP Learning](https://learning.sap.com/learning-journeys/developing-with-sap-integration-suite/explaining-the-clean-core-approach) – Overview of clean core principles, pillars, and the role of SAP Integration Suite.[web:47]
- [Exploring Clean Core Extensibility Best Practices](https://learning.sap.com/courses/practicing-clean-core-extensibility-for-sap-s-4hana-cloud/explaining-extensibility-model-best-practices) – Clean core extensibility model with levels A–D to classify extension quality and technical debt.[web:45]
- [Clean Core Data White Paper – SAP](https://www.sap.com/documents/2025/11/cc60c7be-2c7f-0010-bca6-c68f7e60039b.html) – Guidance on data aspects of clean core when moving to SAP S/4HANA Cloud Private Edition.[web:52]
- [SAP S/4HANA Clean Core Extensibility Guide (PDF)](https://www.scribd.com/document/948735181/Clean-core-extensibility-for-SAP-S-4HANA-Cloud) – Whitepaper describing clean core extensibility levels, upgrade safety, and custom code strategy.[web:53]
- [SAP S/4HANA Extensibility Options for Clean Core Journey](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/14014558) – Blog outlining clean core pillars and how to choose extensibility options.[web:56]
- [SAP S/4HANA Extensibility: An Overview](https://sbpdigital.com/s4hana-extensibility/) – Overview of extensibility options, clean core paradigm, and benefits of an upgrade-stable model.[web:51]

### ABAP Cloud, RAP & Developer Extensibility

- [ABAP Cloud & ABAP RESTful Application Programming Model (RAP) – ASUG PDF](https://blog.asug.com/hubfs/Chapter%20Events/ABAP%20Cloud%20-%20RAP%20-%20S4HANA%20Extensibility.pdf) – Deep dive into RAP, ABAP Cloud, on-stack vs side-by-side extensibility.[web:42]
- [ABAP Extensibility Guide – Clean Core for SAP S/4HANA Cloud](https://community.sap.com/t5/technology-blog-posts-by-sap/abap-extensibility-guide-clean-core-for-sap-s-4hana-cloud-august-2025/ba-p/14009741) – Updated ABAP extensibility guide aligned with clean core levels.[web:48]
- [RAP On-Stack Developer Extensibility](https://community.sap.com/t5/technology-blog-posts-by-members/rap-on-stack-developer-extensibility/ba-p/14017859) – How to extend standard RAP business objects in S/4HANA and BTP ABAP Environment.[web:54]

### Integration & Side-by-Side Extensions

- [What is SAP Integration Suite?](https://help.sap.com/docs/integration-suite/sap-integration-suite/what-is-sap-integration-suite) – Integration Suite as a key enabler of clean core, connecting processes, data, and apps.[web:40]
- [SAP Integration Suite in the Clean Core Approach – SAP Learning](https://learning.sap.com/learning-journeys/developing-with-sap-integration-suite/explaining-the-clean-core-approach) – How clean integration supports clean core with API-first and event-driven patterns.[web:47]
- [How to Build Side-by-Side Extensions for SAP S/4HANA Public Cloud](https://community.sap.com/t5/technology-blog-posts-by-sap/how-to-build-side-by-side-extensions-for-sap-s-4hana-public-cloud-with-sap-btp-abap-environment/ba-p/14011065) – Practical guide to side-by-side extensions with SAP BTP ABAP Environment and S/4HANA cloud trial.[web:49]

> Contributions welcome: opinionated reference architectures combining RAP (on-stack), CAP (side-by-side), Integration Suite, and event-driven patterns for a clean core landscape.

---

## SAP BTP

**[`^ back to top ^`](#table-of-contents)**

### Programming Models & CAP

- [SAP Cloud Application Programming Model (CAP)](https://cap.cloud.sap/docs/) – Official CAP documentation (Node.js and Java).
- [Programming Models – SAP Help Portal](https://help.sap.com/docs/btp/sap-business-technology-platform/cloud-application-programming-model) – Help Portal entry for CAP and related programming models.[web:22]

### CAP Samples & Demo Apps

- [SAP BTP CAP Demo Use Cases](https://github.com/SAP-samples/btp-cap-demo-usecases) – Demo applications showcasing multiple CAP features together with SAP BTP services.[web:33]
- [CAP Samples for Java – Bookshop](https://github.com/SAP-samples/cloud-cap-samples-java) – Sample CAP application in Java (bookshop), including H2/HANA persistence, Fiori UI, and deployment options.[web:38]
- [CAP Sample Repositories (capire)](https://github.com/capire) – Central GitHub org for CAP samples and example projects.[web:44]

> Contributions welcome: multitenancy, XSUAA, destinations, eventing, Kyma, Cloud Foundry deployment examples, GenAI integration, etc.

---

## SAP CPI / Integration

**[`^ back to top ^`](#table-of-contents)**

### SAP Integration Suite

- [What is SAP Integration Suite?](https://help.sap.com/docs/integration-suite/sap-integration-suite/what-is-sap-integration-suite) – Overview of Integration Suite capabilities (Cloud Integration, API Management, Event Mesh, Open Connectors, etc.).[web:40]
- [Integration Suite – SAP Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/integration-suite) – Service description, use cases, missions, and architecture blueprints.[web:43]

### SAP Cloud Integration (CPI)

- [SAP Cloud Integration – Help Portal](https://help.sap.com/docs/cloud-integration/sap-cloud-integration/sap-cloud-integration) – Official documentation for SAP Cloud Integration, including connectivity, security, and scenario configuration.[web:32]
- [What Is SAP Cloud Integration?](https://help.sap.com/docs/cloud-integration/sap-cloud-integration/what-is-sap-cloud-integration) – Conceptual overview and benefits of Cloud Integration.[web:35]

> Contributions welcome: ready-to-use iFlow samples, CPI Groovy/JavaScript script collections, integration patterns (saga, pub/sub, bulk load), and monitoring/troubleshooting guides.

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
