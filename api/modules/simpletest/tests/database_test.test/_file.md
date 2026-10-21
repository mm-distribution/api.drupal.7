# modules/simpletest/tests/database_test.test

- **Source:** [local](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · 4684 lines
- **Module/theme:** batch_test

## Classes and interfaces (derived index)

- [FakeRecord](FakeRecord.md)
- [DatabaseTestCase](DatabaseTestCase.md) — Base test class for databases.
- [DatabaseConnectionTestCase](DatabaseConnectionTestCase.md) — Test connection management.
- [DatabaseSelectCloneTest](DatabaseSelectCloneTest.md) — Test cloning Select queries.
- [DatabaseFetchTestCase](DatabaseFetchTestCase.md) — Test fetch actions, part 1.
- [DatabaseFetch2TestCase](DatabaseFetch2TestCase.md) — Test fetch actions, part 2.
- [DatabaseInsertTestCase](DatabaseInsertTestCase.md) — Test the insert builder.
- [DatabaseInsertLOBTestCase](DatabaseInsertLOBTestCase.md) — Insert tests using LOB fields, which are weird on some databases.
- [DatabaseInsertDefaultsTestCase](DatabaseInsertDefaultsTestCase.md) — Insert tests for "database default" values.
- [DatabaseUpdateTestCase](DatabaseUpdateTestCase.md) — Update builder tests.
- [DatabaseUpdateComplexTestCase](DatabaseUpdateComplexTestCase.md) — Tests for more complex update statements.
- [DatabaseUpdateLOBTestCase](DatabaseUpdateLOBTestCase.md) — Test update queries involving LOB values.
- [DatabaseDeleteTruncateTestCase](DatabaseDeleteTruncateTestCase.md) — Delete/Truncate tests.
- [DatabaseMergeTestCase](DatabaseMergeTestCase.md) — Test the MERGE query builder.
- [DatabaseSelectTestCase](DatabaseSelectTestCase.md) — Test the SELECT builder.
- [DatabaseSelectSubqueryTestCase](DatabaseSelectSubqueryTestCase.md) — Test case for subselects in a dynamic SELECT query.
- [DatabaseSelectOrderedTestCase](DatabaseSelectOrderedTestCase.md) — Test select with order by clauses.
- [DatabaseSelectComplexTestCase](DatabaseSelectComplexTestCase.md) — Test more complex select statements.
- [DatabaseSelectComplexTestCase2](DatabaseSelectComplexTestCase2.md) — Test more complex select statements, part 2.
- [DatabaseSelectPagerDefaultTestCase](DatabaseSelectPagerDefaultTestCase.md)
- [DatabaseSelectTableSortDefaultTestCase](DatabaseSelectTableSortDefaultTestCase.md)
- [DatabaseTaggingTestCase](DatabaseTaggingTestCase.md) — Select tagging tests.
- [DatabaseAlterTestCase](DatabaseAlterTestCase.md) — Select alter tests.
- [DatabaseRegressionTestCase](DatabaseRegressionTestCase.md) — Regression tests.
- [DatabaseLoggingTestCase](DatabaseLoggingTestCase.md) — Query logging tests.
- [DatabaseSerializeQueryTestCase](DatabaseSerializeQueryTestCase.md) — Query serialization tests.
- [DatabaseRangeQueryTestCase](DatabaseRangeQueryTestCase.md) — Range query tests.
- [DatabaseTemporaryQueryTestCase](DatabaseTemporaryQueryTestCase.md) — Temporary query tests.
- [DatabaseBasicSyntaxTestCase](DatabaseBasicSyntaxTestCase.md) — Test how the current database driver interprets the SQL syntax.
- [DatabaseCaseSensitivityTestCase](DatabaseCaseSensitivityTestCase.md) — Test case sensitivity handling.
- [DatabaseInvalidDataTestCase](DatabaseInvalidDataTestCase.md) — Test invalid data handling.
- [DatabaseQueryTestCase](DatabaseQueryTestCase.md) — Drupal-specific SQL syntax tests.
- [DatabaseTransactionTestCase](DatabaseTransactionTestCase.md) — Test transaction support, particularly nesting.
- [DatabaseNextIdCase](DatabaseNextIdCase.md) — Check the sequences API.
- [DatabaseEmptyStatementTestCase](DatabaseEmptyStatementTestCase.md) — Tests the empty pseudo-statement class.
- [ConnectionUnitTest](ConnectionUnitTest.md) — Tests management of database connections.
- [DatabaseReservedKeywordTestCase](DatabaseReservedKeywordTestCase.md) — Test reserved keyword handling (introduced for MySQL 8+)
- [DatabaseTablePrefixTestCase](DatabaseTablePrefixTestCase.md) — Test table prefix handling.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
