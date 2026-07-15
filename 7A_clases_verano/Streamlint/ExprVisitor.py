# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#usingDirective.
    def visitUsingDirective(self, ctx:ExprParser.UsingDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#qualifiedName.
    def visitQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classDeclaration.
    def visitClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classModifier.
    def visitClassModifier(self, ctx:ExprParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#inheritanceList.
    def visitInheritanceList(self, ctx:ExprParser.InheritanceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classBody.
    def visitClassBody(self, ctx:ExprParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#classMember.
    def visitClassMember(self, ctx:ExprParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceBody.
    def visitInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interfaceMember.
    def visitInterfaceMember(self, ctx:ExprParser.InterfaceMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fieldModifier.
    def visitFieldModifier(self, ctx:ExprParser.FieldModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:ExprParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodModifier.
    def visitMethodModifier(self, ctx:ExprParser.MethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#accessModifier.
    def visitAccessModifier(self, ctx:ExprParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameterList.
    def visitParameterList(self, ctx:ExprParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameter.
    def visitParameter(self, ctx:ExprParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type.
    def visitType(self, ctx:ExprParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:ExprParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#memberAccessTarget.
    def visitMemberAccessTarget(self, ctx:ExprParser.MemberAccessTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStatement.
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forStatement.
    def visitForStatement(self, ctx:ExprParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forInit.
    def visitForInit(self, ctx:ExprParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forUpdate.
    def visitForUpdate(self, ctx:ExprParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStatement.
    def visitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#switchStatement.
    def visitSwitchStatement(self, ctx:ExprParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#switchCase.
    def visitSwitchCase(self, ctx:ExprParser.SwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#defaultCase.
    def visitDefaultCase(self, ctx:ExprParser.DefaultCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tryCatchStatement.
    def visitTryCatchStatement(self, ctx:ExprParser.TryCatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#catchClause.
    def visitCatchClause(self, ctx:ExprParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#finallyClause.
    def visitFinallyClause(self, ctx:ExprParser.FinallyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#returnStatement.
    def visitReturnStatement(self, ctx:ExprParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expressionStatement.
    def visitExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#memberAccess.
    def visitMemberAccess(self, ctx:ExprParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalNot.
    def visitLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalAnd.
    def visitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#throwException.
    def visitThrowException(self, ctx:ExprParser.ThrowExceptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableExpr.
    def visitVariableExpr(self, ctx:ExprParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#newObject.
    def visitNewObject(self, ctx:ExprParser.NewObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literalExpr.
    def visitLiteralExpr(self, ctx:ExprParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relational.
    def visitRelational(self, ctx:ExprParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalOr.
    def visitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equality.
    def visitEquality(self, ctx:ExprParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#methodCall.
    def visitMethodCall(self, ctx:ExprParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#argumentList.
    def visitArgumentList(self, ctx:ExprParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal.
    def visitLiteral(self, ctx:ExprParser.LiteralContext):
        return self.visitChildren(ctx)



del ExprParser