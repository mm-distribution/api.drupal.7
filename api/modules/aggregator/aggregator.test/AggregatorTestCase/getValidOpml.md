# AggregatorTestCase::getValidOpml()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 209–240 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L209-L240)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getValidOpml($feeds)
```

## Documentation

```text
Creates a valid OPML file from an array of feeds.

@param $feeds
  An array of feeds.

@return
  Path to valid OPML file.
```

## Code

```php
  function getValidOpml($feeds) {
    // Properly escape URLs so that XML parsers don't choke on them.
    foreach ($feeds as &$feed) {
      $feed['url'] = htmlspecialchars($feed['url']);
    }
    /**
     * Does not have an XML declaration, must pass the parser.
     */
    $opml = <<<EOF
<opml version="1.0">
  <head></head>
  <body>
    <!-- First feed to be imported. -->
    <outline text="{$feeds[0]['title']}" xmlurl="{$feeds[0]['url']}" />

    <!-- Second feed. Test string delimitation and attribute order. -->
    <outline xmlurl='{$feeds[1]['url']}' text='{$feeds[1]['title']}'/>

    <!-- Test for duplicate URL and title. -->
    <outline xmlurl="{$feeds[0]['url']}" text="Duplicate URL"/>
    <outline xmlurl="http://duplicate.title" text="{$feeds[1]['title']}"/>

    <!-- Test that feeds are only added with required attributes. -->
    <outline text="{$feeds[2]['title']}" />
    <outline xmlurl="{$feeds[2]['url']}" />
  </body>
</opml>
EOF;

    $path = 'public://valid-opml.xml';
    return file_unmanaged_save_data($opml, $path);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
