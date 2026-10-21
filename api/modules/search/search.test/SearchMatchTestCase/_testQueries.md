# SearchMatchTestCase::_testQueries()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 99–204 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L99-L204)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function _testQueries()
```

## Documentation

```text
Run predefine queries looking for indexed terms.
```

## Code

```php
  function _testQueries() {
    /*
      Note: OR queries that include short words in OR groups are only accepted
      if the ORed terms are ANDed with at least one long word in the rest of the query.

      e.g. enim dolore OR ut = enim (dolore OR ut) = (enim dolor) OR (enim ut) -> good
      e.g. dolore OR ut = (dolore) OR (ut) -> bad

      This is a design limitation to avoid full table scans.
    */
    $queries = array(
      // Simple AND queries.
      'ipsum' => array(1),
      'enim' => array(4, 5, 6),
      'xxxxx' => array(),
      'enim minim' => array(5, 6),
      'enim xxxxx' => array(),
      'dolore eu' => array(7),
      'dolore xx' => array(),
      'ut minim' => array(5),
      'xx minim' => array(),
      'enim veniam am minim ut' => array(5),
      // Simple OR queries.
      'dolore OR ipsum' => array(1, 2, 7),
      'dolore OR xxxxx' => array(2, 7),
      'dolore OR ipsum OR enim' => array(1, 2, 4, 5, 6, 7),
      'ipsum OR dolore sit OR cillum' => array(2, 7),
      'minim dolore OR ipsum' => array(7),
      'dolore OR ipsum veniam' => array(7),
      'minim dolore OR ipsum OR enim' => array(5, 6, 7),
      'dolore xx OR yy' => array(),
      'xxxxx dolore OR ipsum' => array(),
      // Negative queries.
      'dolore -sit' => array(7),
      'dolore -eu' => array(2),
      'dolore -xxxxx' => array(2, 7),
      'dolore -xx' => array(2, 7),
      // Phrase queries.
      '"dolore sit"' => array(2),
      '"sit dolore"' => array(),
      '"am minim veniam es"' => array(6, 7),
      '"minim am veniam es"' => array(),
      // Mixed queries.
      '"am minim veniam es" OR dolore' => array(2, 6, 7),
      '"minim am veniam es" OR "dolore sit"' => array(2),
      '"minim am veniam es" OR "sit dolore"' => array(),
      '"am minim veniam es" -eu' => array(6),
      '"am minim veniam" -"cillum dolore"' => array(5, 6),
      '"am minim veniam" -"dolore cillum"' => array(5, 6, 7),
      'xxxxx "minim am veniam es" OR dolore' => array(),
      'xx "minim am veniam es" OR dolore' => array()
    );
    foreach ($queries as $query => $results) {
      $result = db_select('search_index', 'i')
        ->extend('SearchQuery')
        ->searchExpression($query, SEARCH_TYPE)
        ->execute();

      $set = $result ? $result->fetchAll() : array();
      $this->_testQueryMatching($query, $set, $results);
      $this->_testQueryScores($query, $set, $results);
    }

    // These queries are run against the second index type, SEARCH_TYPE_2.
    $queries = array(
      // Simple AND queries.
      'ipsum' => array(),
      'enim' => array(),
      'enim minim' => array(),
      'dear' => array(8),
      'germany' => array(11, 12),
    );
    foreach ($queries as $query => $results) {
      $result = db_select('search_index', 'i')
        ->extend('SearchQuery')
        ->searchExpression($query, SEARCH_TYPE_2)
        ->execute();

      $set = $result ? $result->fetchAll() : array();
      $this->_testQueryMatching($query, $set, $results);
      $this->_testQueryScores($query, $set, $results);
    }

    // These queries are run against the third index type, SEARCH_TYPE_JPN.
    $queries = array(
      // Simple AND queries.
      '呂波耳' => array(13),
      '以呂波耳' => array(13),
      'ほへと　ヌルヲ' => array(13),
      'とちリ' => array(),
      'ドルーパル' => array(14),
      'パルが大' => array(14),
      'コーヒー' => array(15),
      'ヒーキ' => array(),
    );
    foreach ($queries as $query => $results) {
      $result = db_select('search_index', 'i')
        ->extend('SearchQuery')
        ->searchExpression($query, SEARCH_TYPE_JPN)
        ->execute();

      $set = $result ? $result->fetchAll() : array();
      $this->_testQueryMatching($query, $set, $results);
      $this->_testQueryScores($query, $set, $results);
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
