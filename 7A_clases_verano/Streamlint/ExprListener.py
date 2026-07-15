# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#usingDirective.
    def enterUsingDirective(self, ctx:ExprParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by ExprParser#usingDirective.
    def exitUsingDirective(self, ctx:ExprParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by ExprParser#qualifiedName.
    def enterQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by ExprParser#qualifiedName.
    def exitQualifiedName(self, ctx:ExprParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by ExprParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:ExprParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#classDeclaration.
    def enterClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#classDeclaration.
    def exitClassDeclaration(self, ctx:ExprParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#classModifier.
    def enterClassModifier(self, ctx:ExprParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#classModifier.
    def exitClassModifier(self, ctx:ExprParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#inheritanceList.
    def enterInheritanceList(self, ctx:ExprParser.InheritanceListContext):
        pass

    # Exit a parse tree produced by ExprParser#inheritanceList.
    def exitInheritanceList(self, ctx:ExprParser.InheritanceListContext):
        pass


    # Enter a parse tree produced by ExprParser#classBody.
    def enterClassBody(self, ctx:ExprParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#classBody.
    def exitClassBody(self, ctx:ExprParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#classMember.
    def enterClassMember(self, ctx:ExprParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by ExprParser#classMember.
    def exitClassMember(self, ctx:ExprParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:ExprParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceBody.
    def enterInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceBody.
    def exitInterfaceBody(self, ctx:ExprParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by ExprParser#interfaceMember.
    def enterInterfaceMember(self, ctx:ExprParser.InterfaceMemberContext):
        pass

    # Exit a parse tree produced by ExprParser#interfaceMember.
    def exitInterfaceMember(self, ctx:ExprParser.InterfaceMemberContext):
        pass


    # Enter a parse tree produced by ExprParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:ExprParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#fieldModifier.
    def enterFieldModifier(self, ctx:ExprParser.FieldModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#fieldModifier.
    def exitFieldModifier(self, ctx:ExprParser.FieldModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:ExprParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:ExprParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:ExprParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#methodModifier.
    def enterMethodModifier(self, ctx:ExprParser.MethodModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#methodModifier.
    def exitMethodModifier(self, ctx:ExprParser.MethodModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#accessModifier.
    def enterAccessModifier(self, ctx:ExprParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by ExprParser#accessModifier.
    def exitAccessModifier(self, ctx:ExprParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by ExprParser#parameterList.
    def enterParameterList(self, ctx:ExprParser.ParameterListContext):
        pass

    # Exit a parse tree produced by ExprParser#parameterList.
    def exitParameterList(self, ctx:ExprParser.ParameterListContext):
        pass


    # Enter a parse tree produced by ExprParser#parameter.
    def enterParameter(self, ctx:ExprParser.ParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#parameter.
    def exitParameter(self, ctx:ExprParser.ParameterContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:ExprParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:ExprParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by ExprParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:ExprParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:ExprParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#memberAccessTarget.
    def enterMemberAccessTarget(self, ctx:ExprParser.MemberAccessTargetContext):
        pass

    # Exit a parse tree produced by ExprParser#memberAccessTarget.
    def exitMemberAccessTarget(self, ctx:ExprParser.MemberAccessTargetContext):
        pass


    # Enter a parse tree produced by ExprParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:ExprParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStatement.
    def enterIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStatement.
    def exitIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#forStatement.
    def enterForStatement(self, ctx:ExprParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#forStatement.
    def exitForStatement(self, ctx:ExprParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#forInit.
    def enterForInit(self, ctx:ExprParser.ForInitContext):
        pass

    # Exit a parse tree produced by ExprParser#forInit.
    def exitForInit(self, ctx:ExprParser.ForInitContext):
        pass


    # Enter a parse tree produced by ExprParser#forUpdate.
    def enterForUpdate(self, ctx:ExprParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by ExprParser#forUpdate.
    def exitForUpdate(self, ctx:ExprParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStatement.
    def enterWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStatement.
    def exitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#switchStatement.
    def enterSwitchStatement(self, ctx:ExprParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#switchStatement.
    def exitSwitchStatement(self, ctx:ExprParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#switchCase.
    def enterSwitchCase(self, ctx:ExprParser.SwitchCaseContext):
        pass

    # Exit a parse tree produced by ExprParser#switchCase.
    def exitSwitchCase(self, ctx:ExprParser.SwitchCaseContext):
        pass


    # Enter a parse tree produced by ExprParser#defaultCase.
    def enterDefaultCase(self, ctx:ExprParser.DefaultCaseContext):
        pass

    # Exit a parse tree produced by ExprParser#defaultCase.
    def exitDefaultCase(self, ctx:ExprParser.DefaultCaseContext):
        pass


    # Enter a parse tree produced by ExprParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:ExprParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:ExprParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#catchClause.
    def enterCatchClause(self, ctx:ExprParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by ExprParser#catchClause.
    def exitCatchClause(self, ctx:ExprParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by ExprParser#finallyClause.
    def enterFinallyClause(self, ctx:ExprParser.FinallyClauseContext):
        pass

    # Exit a parse tree produced by ExprParser#finallyClause.
    def exitFinallyClause(self, ctx:ExprParser.FinallyClauseContext):
        pass


    # Enter a parse tree produced by ExprParser#returnStatement.
    def enterReturnStatement(self, ctx:ExprParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#returnStatement.
    def exitReturnStatement(self, ctx:ExprParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#expressionStatement.
    def enterExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#expressionStatement.
    def exitExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#memberAccess.
    def enterMemberAccess(self, ctx:ExprParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#memberAccess.
    def exitMemberAccess(self, ctx:ExprParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalNot.
    def enterLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalNot.
    def exitLogicalNot(self, ctx:ExprParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalAnd.
    def enterLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalAnd.
    def exitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by ExprParser#addSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#addSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#throwException.
    def enterThrowException(self, ctx:ExprParser.ThrowExceptionContext):
        pass

    # Exit a parse tree produced by ExprParser#throwException.
    def exitThrowException(self, ctx:ExprParser.ThrowExceptionContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#variableExpr.
    def enterVariableExpr(self, ctx:ExprParser.VariableExprContext):
        pass

    # Exit a parse tree produced by ExprParser#variableExpr.
    def exitVariableExpr(self, ctx:ExprParser.VariableExprContext):
        pass


    # Enter a parse tree produced by ExprParser#newObject.
    def enterNewObject(self, ctx:ExprParser.NewObjectContext):
        pass

    # Exit a parse tree produced by ExprParser#newObject.
    def exitNewObject(self, ctx:ExprParser.NewObjectContext):
        pass


    # Enter a parse tree produced by ExprParser#literalExpr.
    def enterLiteralExpr(self, ctx:ExprParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by ExprParser#literalExpr.
    def exitLiteralExpr(self, ctx:ExprParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by ExprParser#relational.
    def enterRelational(self, ctx:ExprParser.RelationalContext):
        pass

    # Exit a parse tree produced by ExprParser#relational.
    def exitRelational(self, ctx:ExprParser.RelationalContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalOr.
    def enterLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalOr.
    def exitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by ExprParser#equality.
    def enterEquality(self, ctx:ExprParser.EqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#equality.
    def exitEquality(self, ctx:ExprParser.EqualityContext):
        pass


    # Enter a parse tree produced by ExprParser#methodCall.
    def enterMethodCall(self, ctx:ExprParser.MethodCallContext):
        pass

    # Exit a parse tree produced by ExprParser#methodCall.
    def exitMethodCall(self, ctx:ExprParser.MethodCallContext):
        pass


    # Enter a parse tree produced by ExprParser#argumentList.
    def enterArgumentList(self, ctx:ExprParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentList.
    def exitArgumentList(self, ctx:ExprParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass



del ExprParser