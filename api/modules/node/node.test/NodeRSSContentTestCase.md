# NodeRSSContentTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 943–1000 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L943-L1000)
- **Module/theme:** node

## Signature

```php
class NodeRSSContentTestCase extends DrupalWebTestCase
```

## Documentation

```text
Ensures that data added to nodes by other modules appears in RSS feeds.

Create a node, enable the node_test module to ensure that extra data is
added to the node->content array, then verify that the data appears on the
sitewide RSS feed at rss.xml.
```

## Methods (derived index)

- [getInfo()](NodeRSSContentTestCase/getInfo.md)
- [setUp()](NodeRSSContentTestCase/setUp.md)
- [testNodeRSSContent()](NodeRSSContentTestCase/testNodeRSSContent.md) — Ensures that a new node includes the custom data when added to an RSS feed.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
