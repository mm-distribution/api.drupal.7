# modules/node/node.test

- **Source:** [local](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · 3128 lines
- **Module/theme:** node

## File documentation

```text
@file
Tests for node.module.
```

## Classes and interfaces (derived index)

- [NodeWebTestCase](NodeWebTestCase.md) — Defines a base class for testing the Node module.
- [NodeLoadMultipleTestCase](NodeLoadMultipleTestCase.md) — Test the node_load_multiple() function.
- [NodeLoadHooksTestCase](NodeLoadHooksTestCase.md) — Tests for the hooks invoked during node_load().
- [NodeRevisionsTestCase](NodeRevisionsTestCase.md) — Tests the node revision functionality.
- [PageEditTestCase](PageEditTestCase.md) — Tests the node edit functionality.
- [PagePreviewTestCase](PagePreviewTestCase.md) — Tests the node entity preview functionality.
- [NodeCreationTestCase](NodeCreationTestCase.md) — Tests creating and saving a node.
- [PageViewTestCase](PageViewTestCase.md) — Tests the functionality of node entity edit permissions.
- [SummaryLengthTestCase](SummaryLengthTestCase.md) — Tests the summary length functionality.
- [NodeTitleXSSTestCase](NodeTitleXSSTestCase.md) — Tests XSS functionality with a node entity.
- [NodeBlockTestCase](NodeBlockTestCase.md) — Tests the availability of the syndicate block.
- [NodePostSettingsTestCase](NodePostSettingsTestCase.md) — Checks that the post information displays when enabled for a content type.
- [NodeRSSContentTestCase](NodeRSSContentTestCase.md) — Ensures that data added to nodes by other modules appears in RSS feeds.
- [NodeAccessTestCase](NodeAccessTestCase.md) — Tests basic node_access functionality.
- [NodeAccessRecordsTestCase](NodeAccessRecordsTestCase.md) — Tests hook_node_access_records() functionality.
- [NodeAccessBaseTableTestCase](NodeAccessBaseTableTestCase.md) — Tests for Node Access with a non-node base table.
- [NodeSaveTestCase](NodeSaveTestCase.md) — Tests node save related functionality, including import-save.
- [NodeTypeTestCase](NodeTypeTestCase.md) — Tests related to node types.
- [NodeTypePersistenceTestCase](NodeTypePersistenceTestCase.md) — Test node type customizations persistence.
- [NodeAccessRebuildTestCase](NodeAccessRebuildTestCase.md) — Verifies the rebuild functionality for the node_access table.
- [NodeAdminTestCase](NodeAdminTestCase.md) — Tests node administration page functionality.
- [NodeTitleTestCase](NodeTitleTestCase.md) — Tests node title functionality.
- [NodeFeedTestCase](NodeFeedTestCase.md) — Test the node_feed() functionality.
- [NodeBlockFunctionalTest](NodeBlockFunctionalTest.md) — Functional tests for the node module blocks.
- [MultiStepNodeFormBasicOptionsTest](MultiStepNodeFormBasicOptionsTest.md) — Tests basic options of multi-step node forms.
- [NodeBuildContent](NodeBuildContent.md) — Test to ensure that a node's content is always rebuilt.
- [NodeQueryAlter](NodeQueryAlter.md) — Tests node_query_node_access_alter().
- [NodeEntityFieldQueryAlter](NodeEntityFieldQueryAlter.md) — Tests node_query_entity_field_access_alter().
- [NodeTokenReplaceTestCase](NodeTokenReplaceTestCase.md) — Test node token replacement in strings.
- [NodeRevisionPermissionsTestCase](NodeRevisionPermissionsTestCase.md) — Tests user permissions for node revisions.
- [NodeAccessPagerTestCase](NodeAccessPagerTestCase.md) — Tests pagination with a node access module enabled.
- [NodeAccessFieldTestCase](NodeAccessFieldTestCase.md) — Tests the interaction of the node access system with fields.
- [NodeEntityViewModeAlterTest](NodeEntityViewModeAlterTest.md) — Tests changing view modes for nodes.
- [NodePageCacheTest](NodePageCacheTest.md) — Tests the cache invalidation of node operations.
- [NodeMultiByteUtf8Test](NodeMultiByteUtf8Test.md) — Tests that multi-byte UTF-8 characters are stored and retrieved correctly.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
